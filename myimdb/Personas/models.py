"""Modelos de entidades Personas"""

from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

SEXO = [
    ('H', 'Hombre'),
    ('M', 'Mujer')
]


class Tipo(models.Model):
    """
    profesion de la persona, puede ser:
    - Actor
    - Director
    - Guionista
    """
    nombre = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=("Nombre"),
        help_text=("Nombre de la persona"),
    )

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    """
    Pais de la persona
    """
    nombre = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=("Nombre"),
        help_text=("Nombre del pais"),
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = ("Pais")
        verbose_name_plural = ("Paises")

class Persona(models.Model):
    """
    Una persona puede representar a:
    - Actor
    - Director
    - Guionista
    """
    nombre = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=("Nombre"),
        help_text=("Nombre de la persona"),
    )
    apellido = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=("Apellido"),
        help_text=("Apellido de la persona"),
    )
    fecha_nacimiento = models.DateField(
        help_text="Fecha en que nacio",
        null=True
    )
    debut = models.DateField(
        help_text="Fecha en que debuto",
        null=True
    )
    pais = models.ForeignKey(
        Pais,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=("Pais"),
        related_name="persona_pais",
        help_text=("Pais de nacimiento"),
    )
    slugname = AutoSlugField(
        populate_from='apellido',
        unique=True,
        always_update=True,
        db_index=True,
        verbose_name='Slug',
        max_length=350,
        help_text='Slug autogenerado'
    )
    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
        default='H'
    )
    tipo = models.ManyToManyField(
        Tipo,
        verbose_name=("Tipo de persona"),
        help_text=("Tipo: Guinista, Actor, Director, Creador..."),
        blank=True
    )

    def __str__(self):
        return self.nombre + " " + self.apellido