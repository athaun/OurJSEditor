# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-11 20:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program', '0007_auto_20191219_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='collaborators',
            field=models.ManyToManyField(related_name='_program_collaborators_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
