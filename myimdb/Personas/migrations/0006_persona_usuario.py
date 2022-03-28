# Generated by Django 3.2.12 on 2022-03-28 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Personas', '0005_remove_persona_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Usuario del sistema relacionado a la persona'),
            preserve_default=False,
        ),
    ]
