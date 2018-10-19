import json
from django.shortcuts import render
from django.http import JsonResponse
from .aliyun_oss import qrcode_upload
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def qrcode(request):
    if request.method == 'POST':
        data = {}
        try:
            request_data = json.loads(request.body)
            print(request_data)
            qrcode_url = qrcode_upload(request_data['merchant_id'])
            data['qrcode_url'] = qrcode_url
        except Exception as e:
            data['error'] = e
        return JsonResponse(data)
    return JsonResponse({'error': 'wrong method'})
