# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0002_auto_20151207_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='voters',
            field=models.ManyToManyField(related_name='liked_stories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='story',
            name='moderator',
            field=models.ForeignKey(related_name='moderated_stories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='story',
            field=models.ForeignKey(related_name='comments', to='stories.Story'),
        ),
    ]
