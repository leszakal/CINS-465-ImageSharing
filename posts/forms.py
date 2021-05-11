from django import forms
from django.core import validators
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from posts.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label_suffix='')
    description = forms.CharField(label_suffix='', max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 5}))
    private_status = forms.BooleanField(label='Require login to view', label_suffix='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta():
        model = Post
        fields = ("image", "title", "description", "tags", "private_status")

class CommentForm(forms.Form):
    comment = forms.CharField(label='', max_length=400, widget=forms.Textarea(attrs={'rows': 4, "placeholder":"Write a comment."}))
