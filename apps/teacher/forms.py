from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateTeacherForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label='Nombre de usuario', help_text="user")
    ci = forms.CharField(max_length=10, label="Cédula de identidad", help_text="id")
    first_name = forms.CharField(max_length=30, required=False, label='Nombre', help_text="smile")
    last_name = forms.CharField(max_length=30, required=False, label="Apellido", help_text="wallet")
    email = forms.EmailField(max_length=254, label="Correo electrónico", help_text="mail")
    password1 = forms.CharField(max_length=30, required=True, label="Contraseña", help_text="key", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, required=True, label="Repita la contraseña", help_text="key", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'ci', 'first_name', 'last_name', 'email', 'password1', 'password2')
