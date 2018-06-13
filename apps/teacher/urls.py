
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
    path('seeTheme/<int:id>/', views.seeTheme, name='seeTheme'),
    path('createTheme/', views.createTheme, name='createTheme'),
    path('createNewTheme/', views.createNewTheme, name='createNewTheme'),
    path('editTheme/<int:id>/', views.editTheme, name='editTheme'),
    path('deleteTheme/<int:id>/', views.deleteTheme, name='deleteTheme'),
    path('editNewTheme/<int:id>/', views.editNewTheme, name='editNewTheme'),


    path('problems/', views.problems, name='problems'),
    path('editProblem/<int:id>/', views.editProblem, name='editProblem'),
    path('createProblem/', views.createProblem, name='createProblem'),
    path('seeProblem/<int:id>/', views.seeProblem, name='seeProblem'),
    path('deleteProblem/<int:id>/', views.deleteProblem, name='deleteProblem'),
    path('createNewProblem/', views.createNewProblem, name='createNewProblem'),
    path('editNewProblem/<int:id>/', views.editNewProblem, name='editNewProblem'),


    path('teachers/', views.teachers, name='teachers'),
    path('seeTeacher/<int:id>/', views.seeTeacher, name='seeTeacher'),
    path('createTeacher/', views.createTeacher, name='createTeacher'),
    path('createNewTeacher/', views.createNewTeacher, name='createNewTeacher'),
    path('editTeacher/<int:id>/', views.editTeacher, name='editTeacher'),
    path('deleteTeacher/<int:id>/', views.deleteTeacher, name='deleteTeacher'),
    path('editNewTeacher/<int:id>/', views.editNewTeacher, name='editNewTeacher'),


    path('profile/', views.profile, name='profile'),
    
    path('logout/', views.logout_teacher, name='logoutTeacher'),

]
