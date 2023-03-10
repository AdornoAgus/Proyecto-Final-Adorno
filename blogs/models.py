from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    contenido = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categorias = models.ManyToManyField('Categoria')
    featured = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='post_imagenes/' ,blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    
    class meta:
        ordering = ["-date_created"]

    def get_absolute_url(self):
        return reverse("blogs:post", kwargs={"slug":self.slug})
    
    


    
    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    titulo = models.CharField(max_length=300)
    slug = models.SlugField(unique=True) 
    
    def get_absolute_url(self):
        return reverse("blogs:post", kwargs={"slug":self.slug})
    


    def __str__(self):
        return self.titulo   


