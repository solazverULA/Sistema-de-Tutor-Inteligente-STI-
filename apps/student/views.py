# from django.shortcuts import render
import os, subprocess
from django.conf import settings
from django.core.files import File
from django.contrib.auth import logout as core_logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, ProblemForm, StudentProfileForm
from django.contrib.auth.decorators import login_required
from apps.student.models import *


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
def theme(request):

    learned = list(LearningTheme.objects.filter(student=request.user.people.student).order_by('pk'))
    print (vars(learned[0]))
    return render(request, 'student/theme.html', {'themes': learned})


@login_required
def problem(request):

    progress = Progress.objects.filter(student=request.user.people.student)
    # values_list('id', flat=True).order_by('id')
    # Book.objects.select_related('author__hometown').get(id=4) retorna la ciudad
    print(Difficult.objects.all().values())

    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            try:
                os.mkdir(os.path.join(settings.MEDIA_ROOT, 'compile'))
            except FileExistsError:
                pass

            f = open(os.path.join(settings.MEDIA_ROOT, 'compile', 'to_compile.c'), 'w')
            code_file = File(f)
            code_file.write(form.cleaned_data.get('code'))
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
            print(status)
            print(res)
    else:
        form = ProblemForm()
    return render(request, 'student/problem.html', {'form': form})


@login_required
def user_view(request):
    form = ProblemForm()
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
    return render(request, 'student/user.html', {'form': form})


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
    return render(request, 'student/results.html')


@login_required
def editor(request):
    return render(request, 'student/editor.html')
