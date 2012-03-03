__author__ = 'yin'
from django.conf.urls.defaults import *
from blog.models import Article
from views import *

info_dict = {
    'queryset': Article.objects.order_by("-published_at").all(),
    }

urlpatterns = patterns('',
    (r'^article/list/$', list_article),
    (r'^article/view/(?P<id>[^/])/$', view_article),
    (r'^article/edit/(?P<id>[^/])/$', edit_article),
    (r'^article/delete/(?P<id>[^/])/$', delete_article),
    (r'^article/create/$', create_article),

    (r'category/create/$', create_category),
    (r'category/view/(?P<id>[^/]+)/$', view_category),
    (r'category/edit/(?P<id>[^/]+)/$', edit_category),
    (r'category/delete/(?P<id>[^/]+)/$', delete_category),
    (r'category/list/$', list_category),
)