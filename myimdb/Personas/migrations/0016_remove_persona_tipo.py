# Generated by Django 3.2.12 on 2022-04-30 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0015_persona_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='tipo',
        ),
    ]
