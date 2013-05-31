from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'estim9.views.home', name='home'),
    # url(r'^estim9/', include('estim9.foo.urls')),
	url(r'^hello/$', 'estim9.views.hello'),
	url(r'^gvtest/$', 'graph.views.gvtest'),
	url(r'^gvtest2/$', 'graph.views.gvtest2'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()