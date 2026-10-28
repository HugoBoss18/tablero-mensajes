# mensajes/views.py
from django.views.generic import ListView

from .models import Mensaje


class VistaInicio(ListView):
    model = Mensaje
    template_name = "inicio.html"
    context_object_name = "mensajes"