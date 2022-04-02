# Generated by Django 3.2.12 on 2022-04-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0006_persona_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='usuario',
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(blank=True, help_text='Apellido de la persona', max_length=90, null=True, verbose_name='Apellido'),
        ),
        migrations.AddField(
            model_name='persona',
            name='nombre',
            field=models.CharField(blank=True, help_text='Nombre de la persona', max_length=90, null=True, verbose_name='Nombre'),
        ),
    ]
