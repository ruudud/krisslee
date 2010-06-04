#encoding: utf-8
import os

from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
 
#cache for half a day
@cache_page(43200)
def front(request):
    images = os.listdir(settings.MEDIA_ROOT + 'pics/')
    pictures = [f for f in images if f[-3:] == 'jpg']
    
    #TODO: Find more efficient way of doing this
    w_file = open(settings.CURRENT_WEATHER, 'r')
    w = w_file.readline().split(';')
    w_file.close()
    symbol = None
    desc = None
    if w[0] != 'error':
        symbol = w[0]
        desc = w[1]

    return render_to_response('frontpage.html', 
        {
            'pictures': pictures, 
            'yr_symbol': symbol,
            'yr_desc': desc,
        }, 
        context_instance=RequestContext(request))
