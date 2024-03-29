from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    url(r'^get/$', 'views.get', name='ajax_get'),
    # url(r'^glownem/', include('glownem.foo.urls')),

	url(r'^location/(?P<lat>-?\d+\.\d+),(?P<dx>\d+\.\d+)/(?P<long>-?\d+\.\d+),(?P<dy>\d+\.\d+)/$', 'movies.views.location'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()