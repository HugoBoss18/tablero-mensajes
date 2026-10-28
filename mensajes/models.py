# mensajes/models.py
from django.db import models


class Mensaje(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField("fecha de publicación", auto_now_add=True)  # nuevo

    class Meta:  # nuevo
        ordering = ["-fecha"]

    def __str__(self):
        return self.texto[:50]