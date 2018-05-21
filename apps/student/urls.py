from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.table, name='table'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
