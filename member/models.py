from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields =['username','password']
