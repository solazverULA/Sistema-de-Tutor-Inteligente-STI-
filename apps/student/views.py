# from django.shortcuts import render
import os
import psutil
import statistics
import codecs
import subprocess
from django.conf import settings
from django.core.files import File
from django.contrib.auth import logout as core_logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, ProblemForm, StudentProfileForm
from django.contrib.auth.decorators import login_required
from apps.student.models import *


def agent_heuristics(problem_iter):
    prob_h = []
    prob_max = []

    for prob in problem_iter:
        prob_h.append([prob[0], statistics.mean(prob[1]), statistics.stdev(prob[1]) ])

    # maximo de medias
    prob_max = [max(prob_h, key=lambda item: item[1])]

    # minimo de desviaciones (mas balanceado)
    return [min(prob_max, key=lambda item: item[2])]


def if_approved(progress, dif_problem):
    new_progress = []

    for pr, dif in zip(progress, dif_problem):
        new_progress.append(max(pr.value, dif))

    return new_progress


def increase_score(score):
    if score <= 25:
        return -2

    if 25 < score <= 45:
        return -1

    if 45 < score <= 55:
        return 0

    if 55 < score <= 75:
        return 1

    if score > 75:
        return 2


def calculate_next_problem(request, score=None):
    themes = Theme.objects.all().count()
    progress = Progress.objects.filter(student=request.user.people.student)
    # values_list('id', flat=True).order_by('id')
    problems = list()
    for prob in Problem.objects.all():
        diff_count = 0

        for pr in progress:
            if score:
                diff_count += Difficult.objects.filter(problem=prob,
                                                       theme=pr.theme,
                                                       value__lte=(
                                                           pr.value
                                                           if pr.value == 0 else
                                                           (pr.value +
                                                            increase_score(score)))).count()

            else:
                diff_count += Difficult.objects.filter(problem=prob,
                                                       theme=pr.theme,
                                                       value__lte=pr.value).count()

        if diff_count == themes:
            """
                Dado que tengo UN problema que pertenece a un conjunto de 
                problemas para Actuales o Futuras dificultades (en caso de que 
                resolvio), necesito saber como queda el progreso del usuario si 
                resuelve dicha dificultad (solo si hubo un resultado -score- )
                
                Uso la funcion if_approve(progreso, dif_problemas)  
            """
            if score:
                diff_problem = Difficult.objects.filter(problem=prob).\
                    values_list('value', flat=True).order_by('id')
                problems.append([prob, if_approved(progress, diff_problem)])

            else:
                problems.append([prob, Difficult.objects.filter(problem=prob).
                            values_list('value', flat=True).order_by('id')])

    problems = agent_heuristics(problems)

    return problems[0][0]


def update_student_progress(request, render_problem, result):
    print(render_problem)
    # if len(result['errors']) > 0:
    making_problem = None
    try:
        making_problem = MakingProblem.objects.get(student=request.user.people.
                                                   student,
                                                   problem=render_problem)
    except MakingProblem.DoesNotExist:
        making_problem = MakingProblem.objects.create(student=request.user.
                                                      people.student,
                                                      problem=render_problem,
                                                      score=0)

    # Compilation ERROR -5% in score
    if len(result['errors']) > 0:
        if making_problem.score >= 5:
            making_problem.score -= 5

    if len(result['results']) > 0:
        if len(result['results'][0]) == len(result['results'][1]):
            proportion = 0

            for (user_res, output) in zip(result['results'][0],
                                          result['results'][1]):
                if user_res == output:
                    proportion += 1

            making_problem.score = (proportion*100)/len(result['results'][1])

        else:
            making_problem.score = 0.0

    making_problem.save()

    """
    ################ Inteligent Agent decisions for update Progress ############
    """

    if making_problem.score >= 50.0:
        difficults = Difficult.objects.filter(problem=render_problem)\
            .exclude(value=0)

        for dif in difficults:
            progress = Progress.objects.get(
                student=request.user.people.student, theme=dif.theme)
            progress.value = max(dif.value, progress.value)
            progress.save()

    else:
        difficults = Difficult.objects.filter(problem=render_problem).exclude(
            value=0)

        for dif in difficults:
            progress = Progress.objects.get(
                student=request.user.people.student, theme=dif.theme)
            progress.value = min(dif.value, progress.value)
            progress.save()

    return making_problem.score


def compile_exec(form, render_problem):
    code = []
    errors = []
    results = []

    ############# COMPILACION Y EJECUCION ######################
    try:
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'compile'))
    except FileExistsError:
        pass

    f = open(os.path.join(settings.MEDIA_ROOT, 'compile', 'to_compile.c'), 'wb')
    code_file = File(f)
    code_file.write(bytes(form.cleaned_data.get('code'), "UTF-8"))
    code_file.close()

    status, res = subprocess.getstatusoutput('gcc -o "' +
                                             os.path.join(
                                                 settings.MEDIA_ROOT,
                                                 'compile',
                                                 'compiled.exe', ) +
                                             '" "' +
                                             os.path.join(
                                                 settings.MEDIA_ROOT,
                                                 'compile',
                                                 'to_compile.c', ) +
                                             '"'
                                             )
    if status == 0:
        f = open(os.path.join(settings.MEDIA_ROOT, 'compile',
                              'result.txt'), 'w')
        code_file = File(f)
        code_file.write('')
        code_file.close()
        # cmd = ['cmd', '/c', 'node', '-v']

        f_b = open(os.path.join(settings.MEDIA_ROOT, 'compile',
                                'exec.bat'), 'w')
        code_file = File(f_b)

        if render_problem.referenceInput:
            code_file.write('cmd /c ' + '"' + os.path.normpath(os.path.join(
                settings.MEDIA_ROOT,
                'compile',
                'compiled.exe', )) + '"'
                            + ' < ' + '"' +
                            os.path.normpath(render_problem.
                                             referenceInput.path) + '"'
                            + ' > ' + '"' +
                            os.path.normpath(os.path.join(
                                settings.MEDIA_ROOT,
                                'compile',
                                'result.txt')) + '"')
        else:
            code_file.write('cmd /c ' + '"' + os.path.normpath(os.path.join(
                settings.MEDIA_ROOT,
                'compile',
                'compiled.exe', )) + '"'
                            + ' > ' + '"' +
                            os.path.normpath(os.path.join(
                                settings.MEDIA_ROOT,
                                'compile',
                                'result.txt')) + '"')

        code_file.close()

        def to_raw(str):
            strr = '%r' % str
            strr = strr.replace("\'", '\"')
            return codecs.decode(strr, 'unicode_escape')

        cmd = to_raw(os.path.normpath(os.path.join(
            settings.MEDIA_ROOT,
            'compile', 'exec.bat')))
        print(cmd)
        print("===> Exec....")

        try:

            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            stdout, stderr = proc.communicate(timeout=2)
            #print("status_exec")
            str_it = stdout.decode('ascii').split('\n')
            str_ite = [st.strip() for st in str_it if st.strip() != '']
            print(str_ite)
            # print("err_exec")
            # print(stderr)

        except subprocess.TimeoutExpired:
            def kill_proc_tree(pid, including_parent=True):
                parent = psutil.Process(pid)
                children = parent.children(recursive=True)
                for child in children:
                    child.kill()

                if including_parent:
                    parent.kill()

            print(proc.pid)
            kill_proc_tree(proc.pid)
            errors.append((
                          "Entraste en un loop infinito, revisa las "
                          "sentencias 'for', 'while', 'do while' que esten "
                          "en tu codigo",
                          []))
            print("=====> Exec timer end by time.")

        ############# fin EJECUCION pase CORRECTO ######################
        results.append(tuple(line.rstrip('\n') for line in open(
            os.path.join(settings.MEDIA_ROOT, 'compile', 'result.txt'))))
        results.append(tuple(line.rstrip('\n') for line in
                          open(render_problem.referenceOutput.path)))

    else:
        print("++++++ Compile error.")
        errors.append(("Tienes un error de compilacion",
                       [str.replace(os.path.join(
                           settings.MEDIA_ROOT,
                           'compile',
                           'to_compile.c', ), '') for str in res.split("\n")]))
        print(res.split("\n"))

    code.append(form.cleaned_data.get('code'))
    return {'code': code, 'errors': errors, 'results': results}


"""
===============================================================================
===============================================================================
================================ VISTAS ======================================= 
===============================================================================
===============================================================================
"""


def student_required(request):
    try:
        Student.objects.get(user=request.user)
        return render(request, 'student/index.html')

    except Student.DoesNotExist:
        return redirect('/apps/teacher/')


@login_required
def index(request):
    return student_required(request)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            return student_required(request)
    else:
        form = LoginForm()
    return render(request, 'student/login.html', {'form': form})


def logout(request):
    core_logout(request)
    return redirect('/apps/student/login')


@login_required
def theme(request, id):
    learning = None

    if id:
        learning = LearningTheme.objects.get(id=id)
        progress = Progress.objects.get(student=request.user.people.student, theme=learning.theme)
        next = LearningTheme.objects.get(id=id + 1)
        learning.ready = True
        learning.IsDisabled = False
        next.IsDisabled = False

        """
        Updating for Inteligent Agent
        """
        if not progress.value:
            progress.value = 1
            progress.save()
            print(vars(progress))

        learning.save()
        next.save()

    learned = list(LearningTheme.objects.filter(student=request.user.people.student).order_by('pk'))
    progress_it = Progress.objects.filter(student=request.user.people.student). \
        exclude(value=0.0).order_by('id')

    return render(request, 'student/theme.html', {'themes': learned,
                                                  'id': learning.theme.name if id  else '',
                                                  'progress': progress_it
                                                  })


@login_required
def problem(request, id=None):
    print(id) if id else print("No id")
    render_problem = Problem.objects.get(id=id) if id else \
        calculate_next_problem(request)
    results = {'code': [], 'errors': [], 'results': [], 'score': None}

    if request.method == 'POST':

        form = ProblemForm(request.POST)
        if form.is_valid():
            print("================> Entradadashadkajdk:    ===========")
            print(form.cleaned_data['problem_exec'])
            problem = Problem.objects.get(id=form.cleaned_data['problem_exec'])
            results = compile_exec(form, problem)
            results['score'] = update_student_progress(request,
                                                       problem,
                                                       results)
            """
            ========================================================
            AGENT DECISIONS
            ========================================================
            """
            render_problem = calculate_next_problem(request, results['score'])

    form = ProblemForm()

    print(render_problem)
    return render(request, 'student/problem.html',
                  {'form': form,
                   'id': id if id and len(results['errors']) == 0 and request.POST else '',
                   'problem': render_problem,
                   'score': results['score'],
                   'errors': results['errors'].pop() if len(results['errors']) > 0 else '',
                   'code': results['code'].pop() if len(results['code']) > 0 else ''})


@login_required
def user_view(request):
    form = ProblemForm()
    progress = Progress.objects.filter(student=request.user.people.student).\
        exclude(value=0.0).order_by('id')

    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.people.student.ci = form.cleaned_data.get('ci')

            user.save()

            return render(request, 'student/user.html', {'form': form,
                                                         'user': user})

        else:
            print(form.errors)

    return render(request, 'student/user.html', {'form': form,
                                                 'progress': progress})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            # load the People/Student instance created by the signal
            new_student = Student.objects.create(user=user)
            """
            user.people.student.ci = form.cleaned_data.get('ci')
            user.people.student.teacherMentor = form.cleaned_data.get('teacherMentor')
            user.save()
            """
            new_student.ci = form.cleaned_data.get('ci')
            new_student.teacherMentor = form.cleaned_data.get(
                'teacherMentor')
            user.save()
            new_student.save()
            raw_password = form.cleaned_data.get('password1')

            authenticate(username=user.username, password=raw_password)
            # login(request, user)

            return redirect('/apps/student/login')
    else:
        form = SignUpForm()
    return render(request, 'student/signup.html', {'form': form})


@login_required
def results(request):
    results = MakingProblem.objects.filter(student=request.user.people.student).\
        order_by('score')

    progress = Progress.objects.filter(student=request.user.people.student).\
        exclude(value=0.0).order_by('id')

    return render(request, 'student/results.html', {'results': results, 'progress': progress})


@login_required
def seeResult(request, id):
    problem = MakingProblem.objects.get(student=request.user.people.student,
                                        id=id)
    difficults = Difficult.objects.filter(problem=problem.problem)

    return render(request, 'student/seeResult.html', {'problem': problem, 'difficults': difficults})
