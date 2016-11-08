# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161108_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tages',
        ),
        migrations.AddField(
            model_name='post',
            name='tages',
            field=models.ManyToManyField(to='blog.Tags'),
        ),
    ]
