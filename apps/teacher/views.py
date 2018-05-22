from django.shortcuts import render

def index(request):
    return render(request, 'teacher/dashboard.html')

def table(request):
	return render(request, 'teacher/table.html')

def user(request):
	return render(request, 'teacher/user.html')
