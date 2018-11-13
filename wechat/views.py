from django.shortcuts import render
from django.http import HttpResponse
import hashlib

# Create your views here.


def index(request):
    data = request.GET
    token = 'fanyoutech'
    signature = data.get('signature')
    timestamp = data.get('timestamp')
    nonce = data.get('nonce')
    echostr = data.get('echostr')
    s = [token, timestamp, nonce]
    s.sort()
    s = ''.join(s)
    if hashlib.sha1(s.encode('UTF-8')).hexdigest() == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse('error')