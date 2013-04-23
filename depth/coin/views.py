import json
import urllib2

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils import simplejson

def index(request):

    return render(request, 'index.html')


def ask(request):
    if request.method == "GET":
        data = urllib2.urlopen('https://btc-e.com/api/2/trc_btc/depth')
        j = json.load(data)


        bids = j['bids']
        asks = j['asks']

        return HttpResponse(simplejson.dumps({'bids': bids,
                                              'asks': asks},))

