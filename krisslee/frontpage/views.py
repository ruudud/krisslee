#encoding: utf-8
from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def front(request):
    return render_to_response('frontpage.html', {}, 
        context_instance=RequestContext(request))
