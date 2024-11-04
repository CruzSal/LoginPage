from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=100, 
                               required=True, 
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                            'class':'form-control'}))

    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                            'class':'form-control'})) #Bootstrap class

    password1 = forms.CharField(required=True, 
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class':'form-control',
                                                                 'data-toggle':'password',
                                                                 'id':'password'}))

    password2 = forms.CharField(required=True, 
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password',
                                                                  'class':'form-control',
                                                                  'data-toggle':'password',
                                                                  'id':'password2'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']