from django.shortcuts import render

def index(request):
    return render(request, 'student/dashboard.html')

def login(request):
    return render(request, 'student/login.html')

def table(request):
	return render(request, 'student/table.html')

def user(request):
	return render(request, 'student/user.html')

def register(request):
	return render(request, 'student/register.html')