from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from blogs.models import *
from django.db import models



class PostCommentForm(forms.ModelForm):
    content = forms.CharField(label='Ingres su comentario.')

    class Meta:
        model = Comment
        fields = ['content']

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'overview', 'contenido', 'autor', 'categorias', 'featured', 'imagen']
        labels = {
            'titulo': 'Título',
            'slug': 'Slug',
            'overview': 'Descripción breve',
            'contenido': 'Contenido',
            'autor': 'Autor',
            'categorias': 'Categorías',
            'featured': 'Destacado',
            'imagen': 'Imagen',
        }
        help_texts = {
            'slug': 'El slug sera parte de la URL del post y debe ser unico. No se permiten espacios ni caracteres especiales.',
            'categorias': 'Selecciona las categorias en las que deseas que aparezca el post.',
        }
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(),
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if ' ' in slug:
            raise forms.ValidationError("El slug no puede contener espacios.")
        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Este slug ya está en uso.")
        return slug
