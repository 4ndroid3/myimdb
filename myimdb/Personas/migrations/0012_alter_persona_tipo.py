# Generated by Django 3.2.12 on 2022-04-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0011_persona_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo',
            field=models.ManyToManyField(blank=True, help_text='Tipo: Guinista, Actor, Director, Creador...', to='Personas.Tipo', verbose_name='Tipo de persona'),
        ),
    ]
