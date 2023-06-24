from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Record
#from django.contrib.admin.widgets import AdminDateWidget

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        }


class RecordForm(forms.ModelForm):
     last_visit = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),)
     next_visit = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
     class Meta:
        model = Record
        fields = ('first_name','last_name','phone','city','last_visit','next_visit')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'last_visit': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter last visit date'}),
            'next_visit': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter next visit date'}),
        }
