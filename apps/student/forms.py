from django import forms
from django.forms import ModelChoiceField, Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from apps.teacher.models import Teacher


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True, label='Nombre de Usuario', help_text="study")
    password = forms.CharField(max_length=30, required=True, label="Contraseña", help_text="key", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class TeacherModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Profesor: %s" % (obj.user.username)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label='Nombre de usuario', help_text="user")
    ci = forms.CharField(max_length=10, label="Cédula de identidad", help_text="id")
    first_name = forms.CharField(max_length=30, required=False, label='Nombre', help_text="smile")
    last_name = forms.CharField(max_length=30, required=False, label="Apellido", help_text="wallet")
    email = forms.EmailField(max_length=254, label="Correo electrónico", help_text="mail")
    teacherMentor = TeacherModelChoiceField(queryset=Teacher.objects.all(), label="Profesor", help_text="study")
    password1 = forms.CharField(max_length=30, required=True, label="Contraseña", help_text="key", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, required=True, label="Repita la contraseña", help_text="key", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'ci', 'first_name', 'last_name', 'email', 'password1', 'password2', 'teacherMentor')


class ProblemForm(Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'style': 'display: none;'}))
