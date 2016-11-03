#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from blog.models import Post # наша модель из blog/models.py

from blog.models import Comment # наша модель из blog/models.py

admin.site.register(Post)
admin.site.register(Comment)