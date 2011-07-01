# coding: utf-8
from django.db.models import Count, Sum
from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from krisslee.contribution.models import Contribution
from krisslee.contribution.forms import ContributionForm

def take(request):
    cs = Contribution.objects.all().order_by('name')
    total = Contribution.objects.aggregate(Sum('amount'), Count('name'))

    if request.method == 'POST':
        take_form = ContributionForm(request.POST)
        if take_form.is_valid():
            take_form.save()

    return render_to_response('contribution.html',
        {
            'take_form': ContributionForm(),
            'contributions': cs,
            'total': total,
        },
        context_instance=RequestContext(request))
