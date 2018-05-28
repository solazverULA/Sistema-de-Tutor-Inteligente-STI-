from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('theme/', views.theme, name='theme'),
    path('problem/', views.problem, name='problem'),
    path('login/', auth_views.LoginView.as_view(template_name='student/login.html',
                                                authentication_form=LoginForm),
                                                name='login'),
    path('signup/', views.signup, name='signup'),
    path('user/', views.user_view, name='user_view'),
    path('results/', views.results, name='results'),
    path('editor/', views.editor, name='editor'),
]
