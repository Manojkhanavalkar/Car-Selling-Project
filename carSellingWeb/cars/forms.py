from django import forms 
from .models import cars

class CarForm(forms.ModelForm):
    class Meta:
        model=cars
        fields=['car_name','text','photo']