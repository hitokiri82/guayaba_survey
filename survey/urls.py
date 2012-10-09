from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^survey/', include('survey.foo.urls')),
    #url(r'^survey/$', 'main.views.index'),
    url(r'^$', 'main.views.index'),
    url(r'^thanks/', 'main.views.thanks'),
    url(r'^registered/', 'main.views.registered'),
    url(r'^status/', 'main.views.status'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG is False:  # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
else:
    urlpatterns += staticfiles_urlpatterns()
