from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'mobile', 'location', 'password1', 'password2']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile No'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }
