#coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from krisslee.gallery.models import Picture

def list(request):
    pictures = Picture.objects.all()

    return render_to_response('frontpage.html',
        {
            'pictures': pictures,
        },
        context_instance=RequestContext(request))
