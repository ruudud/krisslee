#encoding: utf-8
import os

from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

@cache_page(604800)
def front(request):
    images = os.listdir(settings.MEDIA_ROOT + 'pics/')
    pictures = [f for f in images if f[-3:] == 'jpg']

    return render_to_response('frontpage.html', 
        {
            'pictures': pictures, 
        }, 
        context_instance=RequestContext(request))
