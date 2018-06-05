
from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [

	path('table/', views.table, name='table'),
    path('user/', views.user, name='user'),

    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('studentProfile/', views.studentProfile, name='studentProfile'),
    path('themes/', views.themes, name='themes'),
    path('problems/', views.problems, name='problems'),
    path('editProblem/', views.editProblem, name='editProblem'),
    path('createProblem/', views.createProblem, name='createProblem'),

    path('createNewProblem/', views.createNewProblem, name='createNewProblem'),

    path('profile/', views.profile, name='profile'),
]
