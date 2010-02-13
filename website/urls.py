from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from website.views import home, jointask, quittask

urlpatterns = patterns('',
    url(r'$', home, name='home'),
    url(r'join/(?P<taskid>\d+)', jointask, name='jointask'),
    url(r'quit/(?P<taskid>\d+)', quittask, name='quittask'),
    url(r'report/', report, name='report'),
)
