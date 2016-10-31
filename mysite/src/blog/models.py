#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField("data") # дата публикации
    content = models.TextField(max_length=10000) # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name = 'comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	approved_comment = models.BooleanField(default = False)

	def approve(self)
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text

