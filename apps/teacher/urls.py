from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.table, name='table'),
    path('user/', views.user, name='user'),
]
