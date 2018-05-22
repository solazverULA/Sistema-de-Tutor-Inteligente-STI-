from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('theme/', views.theme, name='theme'),
    path('problem/', views.problem, name='problem'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),
    path('results/', views.results, name='results'),
]
