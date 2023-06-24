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


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('first_name','last_name','phone','city','last_visit','next_visit')
