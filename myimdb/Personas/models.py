"""Modelos de entidades Personas"""

from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

SEXO = [
    ('H', 'Hombre'),
    ('M', 'Mujer')
]

class Persona(models.Model):
    """
    Una persona puede representar a:
    - Actor
    - Director
    - Guionista
    """
    fecha_nacimiento = models.DateField(
        help_text="Fecha en que nacio",
        null=True
    )
    debut = models.DateField(
        help_text="Fecha en que debuto",
        null=True
    )
    pais = models.CharField(
        max_length=70,
        null=True
    )
    # usuario = models.ForeignKey(
    #     User,
    #     verbose_name=("Usuario del sistema relacionado a la persona"),
    #     on_delete=models.CASCADE
    # )
    usuario = models.OneToOneField(
        User,
        verbose_name=("Usuario del sistema relacionado a la persona"),
        on_delete=models.CASCADE
    )
    slug = AutoSlugField(
        populate_from='usuario',
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

    def __str__(self):
        return self.usuario.first_name + " " + self.usuario.last_name


    