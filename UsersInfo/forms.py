from .models import Schema
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm the password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SchemaForm(ModelForm):
    class Meta:
        model = Schema
        fields = ['name_schema', 'first_name', 'last_name', 'phone_number', 'email', 'address', 'age', 'job', 'company']
        widgets = {'name_schema': TextInput(attrs={'class': 'form-control', 'id': 'nameSchema', 'name': 'newSchema'}),
                   'first_name': TextInput(attrs={'class': 'form-control', 'id': 'firstName'}),
                   'last_name': TextInput(attrs={'class': 'form-control', 'id': 'lastName'}),
                   'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phoneNumber'}),
                   'email': TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': "you@example.com"}),
                   'address': TextInput(attrs={'class': 'form-control', 'id': 'address', 'placeholder': "1234 Main St"}),
                   'age': TextInput(attrs={'class': 'form-control', 'id': 'age'}),
                   'job': TextInput(attrs={'class': 'form-control', 'id': 'job'}),
                   'company': TextInput(attrs={'class': 'form-control', 'id': 'company'})
                   }
