
from django.views.generic import ListView

from .models import Mensaje


class VistaInicio(ListView):
    model = Mensaje
    template_name = "inicio.html"
    context_object_name = "mensajes"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["cantidad_mensajes"] = contexto["mensajes"].count()
        return contexto
