# Generated by Django 4.0.4 on 2022-07-30 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_project_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
