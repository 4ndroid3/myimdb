""" Vistas de los rodajes en el admin de Django """

from django.contrib import admin
from Rodajes.models import Capitulo, Genero, Pelicula, Serie, Temporada

admin.site.register(Genero)
admin.site.register(Capitulo)
admin.site.register(Temporada)
admin.site.register(Serie)
admin.site.register(Pelicula)

