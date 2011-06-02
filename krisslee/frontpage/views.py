#encoding: utf-8
import os

from django.core.cache import cache
from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
 
def blitz(request):
    return HttpResponse('42', mimetype="text/plain")

def front(request):
    pictures = cache.get('pictures')
    if not pictures:
        #TODO: DB-model for this
        images = os.listdir(settings.MEDIA_ROOT + 'pics/')
        pictures = [f for f in images if f[-3:] == 'jpg']
        if pictures:
            cache.set('pictures', pictures, 86400)
    
    yr_data = cache.get('yr_data')
    if not yr_data:
        yr_data = {}
        try:
            w_file = open(settings.CURRENT_WEATHER, 'r')
            w = w_file.readline().split(';')
            w_file.close()
            if w[0] != 'error':
                yr_data['symbol'] = w[0]
                yr_data['desc'] = w[1]
                yr_data['temp'] = w[2]
                cache.set('yr_data', yr_data, 1800)
        except:
            pass

    return render_to_response('frontpage.html', 
        {
            'pictures': pictures, 
            'yr_data': yr_data,
        }, 
        context_instance=RequestContext(request))
