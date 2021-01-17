from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=60)

    class Meta:
        model=User
        fields=('email', 'first_name', 'middle_name', 'last_name', 'phone_number', 'password1', 'password2')
