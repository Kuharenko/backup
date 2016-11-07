# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161107_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagtopost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='tagtopost',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tages',
            field=models.ForeignKey(default=1, to='blog.TagToPost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tagtopost',
            name='name',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tagtopost',
            name='tags',
            field=models.ManyToManyField(to='blog.Tags'),
        ),
    ]
