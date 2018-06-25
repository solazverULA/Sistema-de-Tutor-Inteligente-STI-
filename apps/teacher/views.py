from django.shortcuts import render, redirect
from apps.student.models import *
from apps.teacher.models import *
from django.contrib.auth import logout as core_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateTeacherForm
from django.core.files.storage import FileSystemStorage


def teacher_required(request):
    try:
        Teacher.objects.get(user=request.user)
        return render(request, 'teacher/index.html')

    except Teacher.DoesNotExist:
        return redirect('/apps/student/')


def table(request):
    return render(request, 'teacher/table.html')


def user(request):
    return render(request, 'teacher/user.html')


@login_required
def index(request):
    #return render(request, 'teacher/index.html')
    return teacher_required(request)


def themes(request):
    themes_ = Theme.objects.all()
    return render(request, 'teacher/themes.html', {'themes':themes_})


def seeTheme(request, id):
    theme = Theme.objects.get(id=id)
    #print(pro)
    return render(request, 'teacher/seeTheme.html', {'theme':theme})


def createTheme(request):
    return render(request, 'teacher/createTheme.html')


def createNewTheme(request):
    print(request.POST)
    print(request.FILES)
    name = request.POST['name']

    myfile = request.FILES['referenceContent']
    fs = FileSystemStorage()
    fs.save(myfile.name, myfile)

    p1 = Theme()
    p1.name = name
    p1.referenceContent = myfile
    p1.save()

    return redirect('/apps/teacher/themes/')


def editTheme(request, id):
    theme = Theme.objects.get(id=id)
    return render(request, 'teacher/editTheme.html', {'theme':theme})


def editNewTheme(request,id):
    print(request.POST)
    name = request.POST['name']
    referenceContent = request.POST['referenceContent']

    p1 = Theme.objects.get(id=id)
    p1.name = name
    p1.referenceContent = referenceContent
    p1.save()
    return redirect('/apps/teacher/themes/')


def deleteTheme(request, id):
    theme = Theme.objects.get(id=id)
    theme.delete()
    #print(pro)
    return redirect('/apps/teacher/themes/')


def problems(request):
    problemas = Problem.objects.all()
    return render(request, 'teacher/problems.html', {'pro':problemas})


def editProblem(request, id):
    pro = Problem.objects.get(id=id)
    return render(request, 'teacher/editProblem.html', {'problem':pro})


def seeProblem(request, id):
    pro = Problem.objects.get(id=id)
    #print(pro)
    return render(request, 'teacher/seeProblem.html', {'problem':pro})


def deleteProblem(request, id):
    pro = Problem.objects.get(id=id)
    pro.delete()
    #print(pro)
    return redirect('/apps/teacher/problems/')


def createProblem(request):

    themes = Theme.objects.all()

    if request.method == 'POST' and request.FILES['referenceOutput']:
        title = request.POST['title']
        description = request.POST['description']

        myfile = request.FILES['referenceOutput']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)

        p1 = Problem()
        p1.title = title
        p1.description = description
        #p1.difficult = request.POST['difficult']
        p1.referenceOutput = myfile
        p1.save()
        return redirect('/apps/teacher/problems/')

    return render(request, 'teacher/createProblem.html', {'themes': themes})


def editNewProblem(request, id):
    print(request.POST)
    title = request.POST['title']
    description = request.POST['description']

    p1 = Problem.objects.get(id=id)
    p1.title = title
    p1.description = description
    p1.difficult = request.POST['difficult']
    # p1.referenceInput = request.POST['referenceInput']
    p1.referenceOutput = request.POST['referenceOutput']
    p1.save()
    return redirect('/apps/teacher/problems/')


def profile(request):
    return render(request, 'teacher/profile.html')



def create_teacher(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            # load the People/Student instance created by the signal
            new_teacher = Teacher.objects.create(user=user)
            new_teacher.ci = form.cleaned_data.get('ci')
            user.save()
            new_teacher.save()
            raw_password = form.cleaned_data.get('password1')

            authenticate(username=user.username, password=raw_password)
            # login(request, user)

            return redirect('/apps/teacher/teachers/')
    else:
        form = CreateTeacherForm()
        try:
            teacher = Teacher.objects.get(user=request.user)
            if teacher.root:
                return render(request, 'teacher/createTeacher.html',
                              {'form': form})
            else:
                return redirect('/apps/teacher/')

        except Teacher.DoesNotExist:
            return redirect('/apps/student/')


def see_teacher(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
        if teacher.root:
            return render(request, 'teacher/seeTeacher.html')
        else:
            return redirect('/apps/teacher/')

    except Teacher.DoesNotExist:
        return redirect('/apps/student/')


def logout_teacher(request):
    core_logout(request)
    return redirect('/apps/student/login')








def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teachers.html', {'teachers':teachers})


def seeTeacher(request, id):
    teacher = Teacher.objects.get(id=id)
    #print(pro)
    return render(request, 'teacher/seeTeacher.html', {'teacher':teacher})


def createTeacher(request):
    return render(request, 'teacher/createTeacher.html')


def createNewTeacher(request):
    print(request.POST)

    username = request.POST['username']
    ci = request.POST['ci']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']

    p1 = Teacher()
    user = User()
    user.username = username
    p1.ci = ci
    p1.root = False
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password)
    user.save()
    p1.user = user
    p1.save()

    return redirect('/apps/teacher/teachers/')


def editTeacher(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'teacher/editTeacher.html', {'teacher':teacher})


def editNewTeacher(request,id):
    print(request.POST)

    username = request.POST['username']
    ci = request.POST['ci']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']

    p1 = Teacher.objects.get(id=id)
    p1.user.username = username
    p1.ci = ci
    p1.user.first_name = first_name
    p1.user.last_name = last_name
    p1.user.email = email
    p1.user.save()
    p1.save()

    return redirect('/apps/teacher/teachers/')


def deleteTeacher(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    #print(pro)
    return redirect('/apps/teacher/teachers/')









def students(request):
    students = Student.objects.all()
    return render(request, 'teacher/students.html', {'students':students})


def seeStudent(request, id):
    student = Student.objects.get(id=id)
    #print(pro)
    return render(request, 'teacher/seeStudent.html', {'student':student})


def createStudent(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/createStudent.html', {'teachers':teachers})


def createNewStudent(request):
    print(request.POST)

    username = request.POST['username']
    ci = request.POST['ci']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    teacherMentor = request.POST['teacherMentor']

    p1 = Student()
    user = User()
    user.username = username
    p1.ci = ci
    p1.root = False
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password)
    user.save()
    p1.user = user
    p1.teacherMentor = Teacher.objects.get(id=teacherMentor)
    p1.save()

    return redirect('/apps/teacher/students/')


def editStudent(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'teacher/editStudent.html', {'student':student})


def editNewStudent(request,id):
    print(request.POST)

    username = request.POST['username']
    ci = request.POST['ci']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']

    p1 = Student.objects.get(id=id)
    p1.user.username = username
    p1.ci = ci
    p1.user.first_name = first_name
    p1.user.last_name = last_name
    p1.user.email = email
    p1.user.save()
    p1.save()

    return redirect('/apps/teacher/students/')


def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    #print(pro)
    return redirect('/apps/teacher/students/')