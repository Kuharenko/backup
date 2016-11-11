# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161108_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catname',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tagtopost',
            name='tags',
        ),
        migrations.DeleteModel(
            name='CatName',
        ),
        migrations.DeleteModel(
            name='TagToPost',
        ),
    ]
