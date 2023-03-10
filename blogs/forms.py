from django import forms
from blogs.models import *


class PostCommentForm(forms.ModelForm):
    content = forms.CharField(label='Ingres su comentario.')

    class Meta:
        model = Comment
        fields = ['content']
