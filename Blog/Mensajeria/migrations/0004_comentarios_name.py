# Generated by Django 4.2.5 on 2023-10-15 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0003_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]
