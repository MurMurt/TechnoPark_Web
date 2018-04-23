
import django.contrib.auth.models as authmodel
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import *


class Login(forms.Form):
    username = forms.CharField(min_length=4, label='Логин', required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')
