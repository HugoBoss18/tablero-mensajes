# mensajes/models.py
from django.db import models


class Mensaje(models.Model):
    texto = models.TextField()