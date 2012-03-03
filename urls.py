from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from TestApp import book_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^DjangoDemo/', include('DjangoDemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './static'}),
)

urlpatterns += patterns ('',
 (r'^depot/', include('depot.urls')),
)

urlpatterns += patterns('',
(r'^blog/', include('blog.urls')),
)

urlpatterns += staticfiles_urlpatterns()