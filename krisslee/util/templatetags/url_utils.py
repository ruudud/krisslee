#coding: utf-8

from django import template

register = template.Library()

@register.simple_tag
def current(request, uri):
    if request.path == uri:
        return 'active'
    else:
        return 'inactive'

