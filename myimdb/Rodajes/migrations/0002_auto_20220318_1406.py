# Generated by Django 3.2.12 on 2022-03-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rodajes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='duracion',
            field=models.DurationField(help_text='Duracion en minutos de el capitulo', null=True),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='nombre',
            field=models.CharField(default='', help_text='Nombre del episodio de la serie', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capitulo',
            name='numero',
            field=models.IntegerField(default=0, help_text='Numero de episodio de la serie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capitulo',
            name='puntuacion',
            field=models.FloatField(max_length=10.0, null=True),
        ),
        migrations.AddField(
            model_name='genero',
            name='nombre',
            field=models.CharField(default='', max_length=90),
            preserve_default=False,
        ),
    ]
