import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from blog.aliyun_oss import qrcode_upload
# Create your views here.


@csrf_exempt
def qrcode(request):
    if request.method == 'POST':
        data = {}
        try:
            request_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'error': 'wrong Content_type '})
        try:
            qrcode_url = qrcode_upload(request_data['merchant_id'])
        except Exception as e:
            return JsonResponse({'error': 'merchant_id not find'})
        data['qrcode_url'] = qrcode_url
        return JsonResponse(data)
    return JsonResponse({'error': 'wrong method'})
