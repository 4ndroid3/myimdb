# Generated by Django 3.2.12 on 2022-04-30 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rodajes', '0027_auto_20220425_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elenco',
            name='actores',
        ),
        migrations.RemoveField(
            model_name='elenco',
            name='directores',
        ),
        migrations.RemoveField(
            model_name='elenco',
            name='guionistas',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='elenco',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='elenco',
        ),
    ]