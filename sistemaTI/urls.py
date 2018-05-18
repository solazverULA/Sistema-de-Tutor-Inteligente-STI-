from django.conf.urls import url
from . import views

app_name = 'sistemaTI'

urlpatterns = [

   url(r'^$', views.index, name='index'),
   url(r'^login/$', views.login, name='login'),
   url(r'^dashboard/$', views.dashboard, name='dashboard'),
   url(r'^estudiantes/$', views.estudiantes, name='estudiantes'),
   url(r'^temas/$', views.temas, name='temas'),
   url(r'^problemas/$', views.problemas, name='problemas'),
   url(r'^editarProblema/$', views.editarProblema, name='editarProblema'),
   url(r'^problema/$', views.problema, name='problema'),

]