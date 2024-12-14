from django import forms 
from .models import cars
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CarForm(forms.ModelForm):
    class Meta:
        model=cars
        fields=['car_name','text','photo']

class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')