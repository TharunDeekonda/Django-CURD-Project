from django import forms
from .models import *

class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"