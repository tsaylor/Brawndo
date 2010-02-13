from django.conf.urls.defaults import *
from website.views import home, jointask, quittask, report

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^twitter/', include('twitter_app.urls')),
#    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^$', home, name='home'),
    url(r'^join/(?P<taskid>\d+)', jointask, name='jointask'),
    url(r'^quit/(?P<taskid>\d+)', quittask, name='quittask'),
    url(r'^report/', report, name='report'),
)

from django.conf import settings
if getattr(settings, 'MEDIA_SERVE', False):
   urlpatterns = patterns('',
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
settings.MEDIA_ROOT}),
   ) + urlpatterns

