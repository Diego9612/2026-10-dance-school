# MODELOS de la app: cada clase es una TABLA de la base de datos.
from django.db import models

__all__ = [
    "School",
]


# class School -> tabla "schoolmanagement_school".
# Cada atributo -> una COLUMNA. Cada objeto School -> una FILA.
# Django anade solo la columna "id" (clave primaria, pk).
class School(models.Model):
    # CharField = texto corto; max_length (obligatorio) = numero maximo de caracteres.
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=2)  # sigla: MO, BO, RE
    zip = models.CharField(max_length=5)  # CAP: texto, no numero (puede empezar por 0)
    country = models.CharField(max_length=100)

    # Campos OPCIONALES:
    #   null=True  -> en la BASE DE DATOS la casilla puede quedar vacia (NULL).
    #   blank=True -> en el FORMULARIO (admin) se puede dejar sin rellenar.
    website = models.URLField(null=True, blank=True)  # valida que sea una URL
    phone = models.CharField(max_length=20, null=True, blank=True)  # texto: +, espacios, 0 inicial
    email = models.EmailField(null=True, blank=True)  # valida que sea un email
    vat = models.CharField(max_length=11, null=True, blank=True)  # partita IVA: 11 cifras

    # Como se muestra una escuela como texto (en el admin, en el shell...).
    # Sin esto veriamos "School object (1)".
    def __str__(self):
        return self.name
