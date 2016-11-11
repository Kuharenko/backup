#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from blog.models import Post  # наша модель из blog/models.py

from blog.models import Comment, Category, Tags, ClickLike  # наша модель из blog/models.py

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(ClickLike)

