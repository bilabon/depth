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
        numerator = request.GET.get('numerator', 'BTC')
        denominator = request.GET.get('denominator', 'USD')

        url = 'https://btc-e.com/api/2/%s_%s/depth'%(numerator.lower(), denominator.lower())
        result = 'success'
        try:
            data = urllib2.urlopen(url)
            j = json.load(data)
            bids = j['bids']
            asks = j['asks']
        except:
            data = urllib2.urlopen('https://btc-e.com/api/2/btc_usd/depth')
            j = json.load(data)
            bids = j['bids']
            asks = j['asks']
            numerator = 'BTC'
            denominator = 'USD'

        return HttpResponse(simplejson.dumps({'bids': bids,
                                              'asks': asks,
                                              'result': result,
                                              'numerator': numerator.upper(),
                                              'denominator': denominator.upper(),
                                             },))

