# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='poster',
            new_name='moderator',
        ),
        migrations.AlterField(
            model_name='story',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
