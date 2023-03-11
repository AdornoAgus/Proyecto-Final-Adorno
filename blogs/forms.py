from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from blogs.models import *




class PostCommentForm(forms.ModelForm):
    content = forms.CharField(label='Ingres su comentario.')

    class Meta:
        model = Comment
        fields = ['content']
