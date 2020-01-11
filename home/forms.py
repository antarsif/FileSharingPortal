from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

from home.models import File, Image


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True)
    username = UsernameField(
        label='Reg. No. :',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2',)

class CreateCourseForm(forms.Form):
    name = forms.CharField(label='Course Name', max_length=40)

'''
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Reg. No. :',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
'''

class Login_form(forms.Form):
    username = forms.CharField(label='Reg. No. :', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file_name','doc','course')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('img_name','img','course')
