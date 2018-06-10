from django.shortcuts import render, redirect
from apps.student.models import *
from apps.teacher.models import *
from django.contrib.auth import logout as core_logout, authenticate

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
	#print(len(problemas))
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
	return render(request, 'teacher/createProblem.html') 

def createNewProblem(request):
	print(request.POST)
	title = request.POST['title']
	description = request.POST['description']

	p1 = Problem()
	p1.title = title
	p1.description = description
	p1.difficult = request.POST['difficult']
	p1.referenceInput = request.POST['referenceInput']
	p1.referenceOutput = request.POST['referenceOutput']
	p1.save()

	return redirect('/apps/teacher/problems/')
	

def editNewProblem(request,id):
	print(request.POST)
	title = request.POST['title']
	description = request.POST['description']

	p1 = Problem.objects.get(id=id)
	p1.title = title
	p1.description = description
	p1.difficult = request.POST['difficult']
	p1.referenceInput = request.POST['referenceInput']
	p1.referenceOutput = request.POST['referenceOutput']
	p1.save()

	return redirect('/apps/teacher/problems/')

def profile(request):
	return render(request, 'teacher/profile.html')

def teachers(request):
	return render(request, 'teacher/teachers.html')

def createTeacher(request):
	return render(request, 'teacher/createTeacher.html')

def seeTeacher(request):
	return render(request, 'teacher/seeTeacher.html')

def logoutTeacher(request):
    core_logout(request)
    return redirect('/apps/student/login')