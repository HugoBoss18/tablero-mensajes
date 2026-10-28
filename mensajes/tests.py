# mensajes/tests.py
from django.test import TestCase
from django.urls import reverse

from .models import Mensaje


class PruebasMensaje(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mensaje = Mensaje.objects.create(texto="Esta es una prueba.")

    def test_contenido_modelo(self):
        self.assertEqual(self.mensaje.texto, "Esta es una prueba.")

    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_pagina_inicio(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "inicio.html")
        self.assertContains(respuesta, "Esta es una prueba.")