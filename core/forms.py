from django import forms
from django.core import validators
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class JoinForm(forms.ModelForm):

    username = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'size':'30',}))
    password = forms.CharField(label_suffix='', widget=forms.PasswordInput(attrs={'size':'30', 'autocomplete':'new-password',}))
    email = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'size':'30',}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'username', 'email', 'password',
            Submit('submit', 'Create Account', css_class="btn btn-info mt-3")
        )

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None
        }

class LoginForm(forms.Form):
    username = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'size':'30',}))
    password = forms.CharField(label_suffix='', widget=forms.PasswordInput(attrs={'size':'30',}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'username', 'password',
            Submit('submit', 'Login', css_class="btn btn-info mt-3")
        )
