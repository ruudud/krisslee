#coding: utf-8
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag
def current(request, uri):
    if not '/' in uri:
        try:
            uri = reverse(uri)
        except NoReverseMatch:
            return 'inactive'

    if request.path == uri:
        return 'active'

    return 'inactive'

