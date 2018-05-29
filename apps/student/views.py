# from django.shortcuts import render
from django.contrib.auth import logout as core_logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'student/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/apps/student/signup')
    else:
        form = LoginForm()
    return render(request, 'student/login.html', {'form': form})


def logout(request):
    core_logout(request)
    return redirect('/apps/student/login')


@login_required
def theme(request):
    return render(request, 'student/theme.html')


@login_required
def problem(request):
    return render(request, 'student/problem.html')


@login_required
def user_view(request):
    return render(request, 'student/user.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the People/Student instance created by the signal
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


@login_required
def results(request):
    return render(request, 'student/results.html')


@login_required
def editor(request):
    return render(request, 'student/editor.html')
