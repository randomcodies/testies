# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-28 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='album',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='album_title',
            new_name='question_text',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='artist',
            new_name='question_title',
        ),
    ]
