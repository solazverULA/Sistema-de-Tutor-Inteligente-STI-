from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from apps.teacher.models import Teacher
from .forms import SignUpForm


def index(request):
    return render(request, 'student/index.html')


def login(request):
    return render(request, 'student/login.html')


def theme(request):
    return render(request, 'student/theme.html')


def problem(request):
    return render(request, 'student/problem.html')


def user_view(request):
    return render(request, 'student/user.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.people.student.ci = form.cleaned_data.get('ci')
            user.people.student.teacherMentor = form.cleaned_data.get('teacherMentor')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            # login(request, user)

            return redirect('/apps/student/login')
    else:
        form = SignUpForm()
    return render(request, 'student/signup.html', {'form': form})


def results(request):
    return render(request, 'student/results.html')


def editor(request):
    return render(request, 'student/editor.html')
