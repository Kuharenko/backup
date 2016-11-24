# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_tags_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tages',
            field=models.ManyToManyField(to='blog.Tags', blank=True),
        ),
    ]
