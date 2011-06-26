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
            return ''

    if request.path == uri:
        return ' class="active"'

    return ''

