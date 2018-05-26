from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.teacher.models import Teacher


class TeacherModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Profesor: %s" % (obj.user.username)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label='Nombre de Usuario.')
    ci = forms.CharField(max_length=10, label="Cédula de Identidad")
    first_name = forms.CharField(max_length=30, required=False, label='Nombre.')
    last_name = forms.CharField(max_length=30, required=False, label="Apellido")
    email = forms.EmailField(max_length=254, label="Correo Electrónico")
    teacherMentor = TeacherModelChoiceField(queryset=Teacher.objects.all())

    """
    password1 = forms.CharField(max_length=30, required=True, label="Contrasenia")
    password2 = forms.CharField(max_length=30, required=True, label="Repita Contrasenia")
    """

    class Meta:
        model = User
        fields = ('username', 'ci', 'first_name', 'last_name', 'email', 'password1', 'password2', 'teacherMentor')