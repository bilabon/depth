from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'depth.views.home', name='home'),
    # url(r'^depth/', include('depth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'depth.coin.views.index', name='index'),
     url(r'^ask$', 'depth.coin.views.ask', name='ask'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                       {'document_root': settings.MEDIA_ROOT}),
)
