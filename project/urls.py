from django.conf.urls.defaults import *
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^twitter/', include('twitter_app.urls')),
    #url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin$', lambda x: HttpResponseRedirect('/admin/')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^', include('website.urls')),
)

from django.conf import settings
if getattr(settings, 'MEDIA_SERVE', False):
   urlpatterns = patterns('',
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
settings.MEDIA_ROOT}),
   ) + urlpatterns

