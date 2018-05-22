from django.shortcuts import render

def index(request):
    return render(request, 'student/dashboard.html')

def login(request):
    return render(request, 'student/login.html')

def theme(request):
	return render(request, 'student/theme.html')

def problem(request):
	return render(request, 'student/problem.html')

def user(request):
	return render(request, 'student/user.html')

def register(request):
	return render(request, 'student/register.html')

def results(request):
	return render(request, 'student/results.html')
