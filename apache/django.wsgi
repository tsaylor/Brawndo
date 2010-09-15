import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

sys.path.insert(0, '/var/django/brawndo')
sys.path.insert(0, '/var/django/brawndo/project')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
