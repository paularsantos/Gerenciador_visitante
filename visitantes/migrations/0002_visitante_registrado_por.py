# Generated by Django 3.2.16 on 2022-11-29 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='registrado_por',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user', verbose_name='Responsável pelo registro'),
            preserve_default=False,
        ),
    ]
