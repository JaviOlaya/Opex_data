from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    
    title = models.CharField(max_length=50, verbose_name="Titulo")
    description = models.TextField(max_length=255, verbose_name="Descripción",blank=True)
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL_friendly")
    order = models.SmallIntegerField(default=0, verbose_name="Orden")
   
    
    class Meta:
        verbose_name="Página"
        verbose_name_plural="Páginas"
    
    def __str__(self):
        return self.title