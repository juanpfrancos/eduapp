from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password1', 'password2', 'role', 'school')
        widgets = {
            'name': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'name':'Name', 'placeholder':'Name', 'aria-label':'Name', 'required':True}),
            'email': forms.EmailInput(attrs={'type':'text', 'class':'form-control', 'name':'email', 'placeholder':'Email', 'aria-label':'Email', 'required':True}),
            'password1': forms.PasswordInput(attrs={'class':'form-control', 'name':'password', 'placeholder':'Password', 'aria-label':'Password', 'required':True}),
            'password2': forms.PasswordInput(attrs={'class':'form-control', 'name':'password', 'placeholder':'Password', 'aria-label':'Password', 'required':True}),
            'role': forms.Select(attrs={'class':'form-control', 'name':'role', 'placeholder':'Role', 'aria-label':'Role', 'required':True}),
            'school': forms.Select(attrs={'class':'form-control', 'name':'school', 'placeholder':'School', 'aria-label':'School', 'required':True}),
        }
class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True, 'type':'text', 'class':'form-control', 'name':'login', 'placeholder':'Login', 'aria-label':'Login', 'autocomplete':'nickname', 'required':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'name':'password', 'placeholder':'Password', 'aria-label':'Password', 'autocomplete':'current-password', 'required':True}))