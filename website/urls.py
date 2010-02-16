from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

from website.models import Assignment

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'join/(?P<taskid>\d+)', 'jointask', name='jointask'),
    url(r'quit/(?P<taskid>\d+)', 'quittask', name='quittask'),
    url(r'report/$', 'report_list', name='report_list'),
    url(r'report/new', 'report_new', name='report_new'),
    url(r'report/(?P<reportid>\d+)', 'report_edit', name='report_edit'),
)
