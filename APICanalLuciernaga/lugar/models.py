from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length = 225)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
