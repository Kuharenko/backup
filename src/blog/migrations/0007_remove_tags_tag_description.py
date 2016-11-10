# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161108_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='tag_description',
        ),
    ]
