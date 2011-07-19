#coding: utf-8
from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from krisslee.gallery.models import Picture

def list(request):
    pictures = cache.get('pictures')
    if not pictures:
        pictures = Picture.objects.all()
        if pictures:
            cache.set('pictures', pictures, 86400)

    return render_to_response('frontpage.html',
        {
            'pictures': pictures,
        },
        context_instance=RequestContext(request))
