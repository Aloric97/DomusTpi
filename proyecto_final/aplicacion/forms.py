from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Turno

User = get_user_model()

class LoginForm(forms.Form):
    usuario = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    # UserCreationForm predeterminado proporciona username, password1 y password2.
    # Incluyendo from django.contrib.auth import User se pueden agregar más campos.

    class Meta:
        model = User
        fields = [    # especifica los campos a renderizar (registro.html) y su orden
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class ProgramarCitaForm(forms.ModelForm):

    class Meta:
        model = Turno
        fields = ['cliente', 'agente', 'dia', 'hora']
        widgets = {'cliente': forms.HiddenInput()}
