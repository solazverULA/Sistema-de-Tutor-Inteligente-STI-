
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
    path('editProblem/<int:id>/', views.editProblem, name='editProblem'),
    path('createProblem/', views.createProblem, name='createProblem'),
    path('seeProblem/<int:id>/', views.seeProblem, name='seeProblem'),
    path('deleteProblem/<int:id>/', views.deleteProblem, name='deleteProblem'),


    path('createNewProblem/', views.createNewProblem, name='createNewProblem'),
    path('editNewProblem/<int:id>/', views.editNewProblem, name='editNewProblem'),

    path('profile/', views.profile, name='profile'),

    path('teachers/', views.teachers, name='teachers'),
    path('createTeacher/', views.createTeacher, name='createTeacher'),
    path('seeTeacher/', views.seeTeacher, name='seeTeacher'),
    path('logout/', views.logoutTeacher, name='logoutTeacher'),

]
