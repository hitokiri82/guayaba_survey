from django.conf.urls import patterns, include, url

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

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
