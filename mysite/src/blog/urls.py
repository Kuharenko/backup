# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from . import views
from blog.views import PostsListView, CommentsListView

urlpatterns = patterns('',
                       url(r'^$', PostsListView.as_view(), name='list'),  # то есть по URL http://имя_сайта/blog/
                       url(r'^(?P<pk>\d+)/$', views.view_post, name='post_detail'),
                       url(r'^admin/new/$', views.post_new, name='post_new'),
                       # а по URL http://имя_сайта/blog/число/
                       url(r'^comm/$', CommentsListView.as_view(), name='comments'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^admin/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
                       url(r'^admin/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
                       url(r'^admin/comm/(?P<rk>[0-9]+)/(?P<pk>[0-9]+)/delete/$', views.comment_delete, name='comment_delete'),
                       url(r'^admin/comm/(?P<pk>[0-9]+)/edit/$', views.comment_edit, name='comment_edit'),
                       url(r'^admin/$', views.adminka, name='admin'),
                       )
