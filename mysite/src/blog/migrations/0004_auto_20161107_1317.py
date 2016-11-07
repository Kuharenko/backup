# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161107_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoty',
            new_name='category',
        ),
    ]
