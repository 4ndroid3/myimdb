"""Modelos de todo lo relacionado con rodajes"""

from autoslug import AutoSlugField
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from Personas.models import Persona



class Genero(models.Model):
    """
    Genero de una pelicula o serie.
    """
    nombre = models.CharField(
        max_length=90
    )

    def __str__(self):
        return self.nombre

class Elenco(models.Model):
    """
    Representacion de un elenco que
    integra un conjunto de personas relacionadas
    con una pelicula o serie
    """
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()
    actores = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="personas_elenco",
        verbose_name=("Personas")
    )
    directores = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="directores_elenco",
        verbose_name=("Directores")
    )
    guionistas = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="guionistas_elenco",
        verbose_name=("Guionistas")
    )

    def __str__(self):
        return "Elenco de la pelicula/serie"
        
class Serie(models.Model):
    """
    Clase que representa una serie en la DB
    """
    nombre = models.CharField(
        max_length=350,
        null=True
    )
    slug = AutoSlugField(
        populate_from='nombre',
        unique=True,
        always_update=True,
        db_index=True,
        verbose_name='Slug',
        max_length=350,
        help_text='Slug autogenerado'
    )
    elenco = models.OneToOneField(
        Elenco,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    generos = models.ManyToManyField(
        Genero,
        blank=True,
        verbose_name=("Generos de la serie")
    )


    def __str__(self):
        return self.nombre


class Temporada(models.Model):
    """
    Representa la temporada/season de una serie
    """
    numero = models.IntegerField(
        verbose_name="Numero de temporada"
    )

    serie = models.ForeignKey(
        Serie,
        on_delete=models.CASCADE,
        related_name="temporadas",
        verbose_name="Serie",
    )

    def __str__(self):
        return self.serie.nombre + " - Temporada " + str(self.numero)


class Capitulo(models.Model):
    """
    Representacion de un capitulo de una serie.
    """
    nombre = models.CharField(
        max_length=250,
        help_text="Nombre del episodio de la serie"
    )
    numero = models.IntegerField(
        help_text="Numero de episodio de la serie",
    )
    duracion = models.DurationField(
        null=True,
        help_text="Duracion en minutos de el capitulo"
    )
    puntuacion = models.FloatField(
        max_length=10.00,
        help_text="Puntuacion del 0.00 al 10.00",
        null=True
    )
    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.CASCADE,
        related_name="capitulos",
        verbose_name="Temporada",
    )

    def __str__(self):
        return str(self.temporada.serie.nombre) + ' - Temporada', str(self.temporada.numero) + " - " + str(self.nombre)


class Pelicula(models.Model):
    """
    Clase que representa una pelicula en la DB
    """
    nombre = models.CharField(
        max_length=350,
        null=True,
        verbose_name="Nombre",
        help_text="Nombre de la Pelicula"
    )
    slug = AutoSlugField(
        populate_from='nombre',
        unique=True,
        always_update=True,
        db_index=True,
        verbose_name='Slug',
        max_length=350,
        help_text='Slug autogenerado'
    )
    duracion = models.DurationField(
        null=True,
        help_text="Duracion en minutos de la pelicula"
    )
    anio = models.PositiveSmallIntegerField(
        null=True,
        verbose_name="Año",
        help_text="Año del estreno",
    )
    elenco = models.ForeignKey(
        Elenco,
        null=True,
        blank=True,
        related_name='elenco_pelicula',
        on_delete=models.CASCADE,
    )
    puntuacion = models.FloatField(
        max_length=10.00,
        null=True,
        help_text="Puntuacion del 0.00 al 10.00"
    )
    generos = models.ManyToManyField(
        Genero,
        blank=True,
        verbose_name=("Generos de la pelicula")
    )

    def __str__(self):
        return self.nombre




    