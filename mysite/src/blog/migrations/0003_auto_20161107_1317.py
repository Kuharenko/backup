# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryToPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='TagToPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categoty',
            field=models.ForeignKey(default=1, to='blog.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tagtopost',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
        migrations.AddField(
            model_name='tagtopost',
            name='tag',
            field=models.ForeignKey(to='blog.Tags'),
        ),
        migrations.AddField(
            model_name='categorytopost',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
