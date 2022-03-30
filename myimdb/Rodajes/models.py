"""Modelos de todo lo relacionado con rodajes"""

from autoslug import AutoSlugField
from django.db import models
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
    elenco = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="serie_elenco",
        verbose_name=("Elenco Actoral de la serie")
    )
    creadores = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="serie_creadores",
        verbose_name=("Creadores de la serie")
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
        unique=True,
        verbose_name="Numero de temporada"
    )

    serie = models.ForeignKey(
        Serie,
        on_delete=models.CASCADE,
        related_name="serie",
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
        related_name="temporada",
        verbose_name="Temporada",
    )

    def __str__(self):
        return self.temporada.numero + " - " + str(self.nombre)

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
    elenco = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="pelicula_elenco",
        verbose_name=("Elenco")
    )
    director = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="pelicula_director",
        verbose_name=("Director/Directores")
    )
    guionista = models.ManyToManyField(
        Persona,
        blank=True,
        related_name="pelicula_guionista",
        verbose_name=("guionistas de la pelicula")
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




    