# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161107_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='viewsq',
            new_name='views_count',
        ),
    ]
