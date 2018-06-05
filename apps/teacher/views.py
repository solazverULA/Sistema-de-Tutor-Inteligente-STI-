from django.shortcuts import render, redirect
from apps.student.models import *
from apps.teacher.models import *

def table(request):
	return render(request, 'teacher/table.html')

def user(request):
	return render(request, 'teacher/user.html')



def index(request):
    return render(request, 'teacher/index.html')

def students(request):
	return render(request, 'teacher/students.html')

def studentProfile(request):
	return render(request, 'teacher/studentProfile.html')
	
def themes(request):
	return render(request, 'teacher/themes.html')
	
def problems(request):

	problemas = Problem.objects.all()
	
	"""p1 = Problem()
	p1.title = "asjhd"
	p1.save()
	print(p1)"""
	print(len(problemas))
	return render(request, 'teacher/problems.html', {'pro':problemas})
	
def editProblem(request):
	return render(request, 'teacher/editProblem.html')

def createProblem(request):
	return render(request, 'teacher/createProblem.html') 

def createNewProblem(request):
	print(request.POST)
	title = request.POST['title']
	description = request.POST['description']

	p1 = Problem()
	p1.title = title
	p1.desdescription = description
	p1.difficult = request.POST['difficult']
	p1.save()

	#return render(request, 'teacher/createProblem.html') 
	return redirect('/apps/teacher/problems/')
	
def profile(request):
	return render(request, 'teacher/profile.html')