import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

sys.path.insert(0, '/var/django/savethisfor.me')
sys.path.insert(0, '/var/django/savethisfor.me/project')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
