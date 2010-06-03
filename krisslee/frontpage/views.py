#encoding: utf-8
import os
import xml.dom.minidom
from datetime import datetime, time

from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
 
def front(request):
    images = os.listdir(settings.MEDIA_ROOT + 'pics/')
    pictures = [f for f in images if f[-3:] == 'jpg']

    doc = xml.dom.minidom.parse(settings.YR_XML)
    tabular = doc.getElementsByTagName('tabular')
    current = tabular[0].getElementsByTagName('time')[0]
    symbol_tag = current.getElementsByTagName('symbol')[0]
    symbol_num = symbol_tag.getAttribute('number')
    if (len(symbol_num) == 1):
        symbol_num = '0%s' % symbol_num
    description = symbol_tag.getAttribute('name')

    cl = time(datetime.now().hour, datetime.now().minute)
    five = time(05, 00)
    eight = time(20, 00)
    symbol = None
    if ((cl > five) and (cl < eight)):
        symbol = '%sd' % symbol_num 
    else:
        symbol = '%sn' % symbol_num 

    return render_to_response('frontpage.html', 
        {
            'pictures': pictures, 
            'yr_symbol': symbol,
            'yr_desc': description,
        }, 
        context_instance=RequestContext(request))
