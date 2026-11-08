# ADMIN: que modelos aparecen en el panel /admin/.
from django.contrib import admin

from schoolmanagement.models import School

# "Registrar" = darlo de alta en el panel. Sin esta linea, School no saldria en /admin/.
admin.site.register(School)
