# Generated by Django 3.2.12 on 2022-03-28 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rodajes', '0011_auto_20220327_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='temporadas',
        ),
    ]
