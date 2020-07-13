from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select

from .models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Phone Number:', widget=forms.TextInput(
        attrs={'class': 'form-control'
               }))
    email = forms.EmailField(max_length=200, label='Email :', widget=forms.TextInput(
        attrs={'class': 'form-control'
               }))
    first_name = forms.CharField(max_length=200, label='First Name :', widget=forms.TextInput(
        attrs={'class': 'form-control'
               }))
    last_name = forms.CharField(max_length=200, label='Last Name :', widget=forms.TextInput(
        attrs={'class': 'form-control'
               }))
    password1 = forms.CharField(max_length=200, label='Password :', widget=forms.PasswordInput(
        attrs={'class': 'form-control'
               }))
    password2 = forms.CharField(max_length=200, label='Confirm Password :', widget=forms.PasswordInput(
        attrs={'class': 'form-control'
               }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=30, label='Phone Number:', widget=forms.TextInput(
        attrs={'class': 'form-control'
               }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input form-control', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input form-control', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input form-control', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input form-control', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Nashik', 'Nashik'),
]
STATE = [
    ('Maharashtra', 'Maharashtra'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ( 'address', 'state', 'city')
        widgets = {
            'address': TextInput(attrs={'class': 'input form-control', 'placeholder': 'address'}),
            'state': Select(attrs={'class': 'input form-control', 'placeholder': 'state'}, choices=STATE),
            'city': Select(attrs={'class': 'input form-control', 'placeholder': 'city'}, choices=CITY),
        }
