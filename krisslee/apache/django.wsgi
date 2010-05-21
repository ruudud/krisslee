import os
import sys

sys.path.append('/home/drit/krisslee.no')
os.environ['DJANGO_SETTINGS_MODULE'] = 'krisslee.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
