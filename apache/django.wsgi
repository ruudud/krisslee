import os
import sys
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(THIS_DIR, '../krisslee')

sys.path.append(PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'krisslee.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
