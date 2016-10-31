#coding: utf-8
from django.conf.urls import patterns, url
from . import views
from blog.views import PostsListView, PostDetailView 

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/ 
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'), # а по URL http://имя_сайта/blog/число/ 
                                              # будет выводиться пост с определенным номером
 url(r'^new/$', views.post_new, name='post_new'),
 url(r'^(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
 url(r'^(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete')
)