# Generated by Django 3.2.12 on 2022-03-28 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rodajes', '0013_auto_20220328_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporada',
            name='numero',
            field=models.IntegerField(unique=True, verbose_name='Numero de temporada'),
        ),
        migrations.AlterField(
            model_name='temporada',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serie', to='Rodajes.serie', verbose_name='Serie'),
        ),
    ]
