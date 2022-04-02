""" Admin de las Personas """

from django.contrib import admin

from Personas.models import Pais, Persona, Tipo

# Register your models here.
admin.site.register(Persona)
admin.site.register(Tipo)
admin.site.register(Pais)

