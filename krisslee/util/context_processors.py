#encoding: utf-8
from django.conf import settings

def icon(request):
    """
    Adds icon url to the context.
    """
    return {'ICON_URL': settings.ICON_URL}
