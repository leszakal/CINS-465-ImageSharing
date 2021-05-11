from django import forms
from django.core import validators
from django.contrib.auth.models import User

class JoinForm(forms.ModelForm):
    username = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'size':'30', 'class':'form-control mb-2 ml-2'}))
    password = forms.CharField(label_suffix='', widget=forms.PasswordInput(attrs={'size':'30', 'autocomplete':'new-password', 'class':'form-control mb-2 ml-2'}))
    email = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'size':'30', 'class':'form-control mb-2 ml-2'}))
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None
        }

class LoginForm(forms.Form):
    username = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'size':'30', 'class':'form-control mb-2 ml-2'}))
    password = forms.CharField(label_suffix='', widget=forms.PasswordInput(attrs={'size':'30', 'class':'form-control mb-2 ml-2'}))
