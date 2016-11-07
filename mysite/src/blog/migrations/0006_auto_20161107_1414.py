# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161107_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytopost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categorytopost',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CategoryToPost',
        ),
    ]
