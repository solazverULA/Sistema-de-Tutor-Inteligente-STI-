from django.shortcuts import render, redirect
from apps.teacher.models import Teacher


def table(request):
    return render(request, 'teacher/table.html')


def user(request):
    return render(request, 'teacher/user.html')


def index(request):
    try:
        Teacher.objects.get(user=request.user)
        return render(request, 'teacher/index.html')

    except Teacher.DoesNotExist:
        return redirect('/apps/student/')


def students(request):
    return render(request, 'teacher/students.html')


def studentProfile(request):
    return render(request, 'teacher/studentProfile.html')


def themes(request):
    return render(request, 'teacher/themes.html')


def problems(request):
    return render(request, 'teacher/problems.html')


def editProblem(request):
    return render(request, 'teacher/editProblem.html')


def profile(request):
    return render(request, 'teacher/profile.html')