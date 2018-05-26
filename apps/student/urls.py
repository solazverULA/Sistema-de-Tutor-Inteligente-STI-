from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('theme/', views.theme, name='theme'),
    path('problem/', views.problem, name='problem'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('user/', views.user_view, name='user_view'),
    path('results/', views.results, name='results'),
    path('editor/', views.editor, name='editor'),
]
