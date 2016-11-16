# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from . import views
handler404 = 'app.views.custom_404'
urlpatterns = patterns('',
                       url(r'^$', views.select_all_posts, name='list'),
                       url(r'^category/$', views.category_list, name='category_list'),
                       url(r'^(?P<post_id>\d+)/$', views.view_post, name='post_detail'),
                       url(r'^admin/new/$', views.post_new, name='post_new'),
                       url(r'^comm/$', views.comments_list, name='comments'),
                       url(r'^admin/(?P<post_id>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
                       url(r'^category/(?P<category_id>[0-9]+)/delete/$', views.cat_delete, name='cat_delete'),
                       url(r'^admin/(?P<post_id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
                       url(r'^admin/comm/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)/delete/$', views.comment_delete,
                           name='comment_delete'),
                       url(r'^admin/post/(?P<post_id>[0-9]+)/comm/(?P<comment_id>[0-9]+)/edit/$', views.comment_edit, name='comment_edit'),
                       url(r'^admin/$', views.adminka, name='admin'),
                       url(r'^(?P<pk>\d+)/addlike/$', views.add_like, name='add_like'),
                       url(r'^category/add/$', views.add_category, name='category'),
                       url(r'^category/edit/(?P<category_id>[0-9]+)$', views.category_edit, name='category_edit'),
                       url(r'^tag/add/$', views.add_tag, name='tag'),
                       url(r'^search/cat/(?P<category_id>[0-9]+)$', views.search_by_category, name='by_category'),
                       url(r'^search/tag/(?P<tag_id>[0-9]+)$', views.search_by_tag, name='by_tag'),
                       url(r'^register/$', views.register, name='registration'),
                       url(r'^login/$', views.log_in, name='login'),
                       url(r'^logout/$', views.logout, name='logout'),
                       url(r'^changepass/$', views.change_pass, name='change_pass'),
                       )

