#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_description = models.TextField()

    def __unicode__(self):
        return self.category_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)
    #tag_description = models.TextField()

    def __unicode__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=255)  # заголовок поста
    datetime = models.DateTimeField("data")  # дата публикации
    content = HTMLField()
    #content = models.TextField(max_length=10000)  # текст поста
    category = models.ManyToManyField(Category)
    tages = models.ManyToManyField(Tags, blank=True)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    def get_likes(self):
        return self.likes_count

    def get_views(self):
        return self.views_count


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __unicode__(self):
        return self.text


class ClickLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.IntegerField(default=0)

    def user_vote(self):
        return self.user

    def __unicode__(self):
        return u"%s" % self.id



