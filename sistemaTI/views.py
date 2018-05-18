# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the sistemati index.")

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def temas(request):
    return render(request, 'temas.html')

def problemas(request):
    return render(request, 'problemas.html')

def editarProblema(request):
    return render(request, 'editarProblema.html')

def problema(request):
    return render(request, 'problema.html')