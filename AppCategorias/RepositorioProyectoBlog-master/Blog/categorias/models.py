from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre
