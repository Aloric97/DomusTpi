from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    usuario = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)
