import hashlib
import random
import re
import json
from urllib import parse
import datetime
from .sql import find_user, update_user, insert_user, find_merchant_user
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
import requests
from .models import Merchant
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
# Create your views here.


def index(request):
    # rows = find_merchant_user()
    # print(rows)
    # print(type(rows))
    return render(request, 'blog/index.html')


# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             dealer_id = request.session.get('dealer_id', None)
#             # if dealer_id == 'None':
#             #     dealer_id = None
#             phone = form.cleaned_data['phone']
#             verify_code = form.cleaned_data['verification_code']
#
#             session_verify_code = request.session.get('verify_code', None)
#             if verify_code == session_verify_code:
#                 try:
#                     del request.session['verify_code']
#                 except KeyError:
#                     pass
#                 row = find_user(phone)
#                 if row:
#                     if dealer_id is None:
#                         return redirect('signup_success')
#                     update_user(phone, dealer_id)
#                     return redirect('signup_success')
#                 else:
#                     insert_user(phone, dealer_id)
#                     return redirect('signup_success')
#             else:
#                 error = "验证码错误"
#                 return render(request, 'blog/signup.html', {'form': form,
#                                                             'error': error})
#     else:
#         dealer_id = request.GET.get('dealer', None)
#         request.session['dealer_id'] = dealer_id
#         form = SignupForm()
#
#     return render(request, 'blog/signup.html', {'form': form})


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request=request)
        if form.is_valid():
            try:
                del request.session['verify_code']
            except KeyError:
                pass
            dealer_id = request.session.get('dealer_id', None)
            phone = form.cleaned_data['phone']
            row = find_user(phone)
            if row:
                if dealer_id is not None:
                    update_user(phone, dealer_id)
                return redirect('signup_success')
            else:
                insert_user(phone, dealer_id)
                return redirect('signup_success')
    else:
        dealer_id = request.GET.get('dealer', None)
        request.session['dealer_id'] = dealer_id
        form = SignupForm()

    return render(request, 'blog/signup.html', {'form': form})


def send_verify_code(request):
    data = {}
    current_time = int(datetime.datetime.now().strftime('%y%m%d%H%M%S'))
    interval_time = current_time - request.session.get('time', 171011091632)
    send_flag = interval_time < 60
    if send_flag:
        data['error_message'] = "重新发送需要%ds时间" % (60-interval_time)
        return JsonResponse(data)
    send_url = 'http://175.25.18.221:8087/sms/v2/std/single_send'
    userid = 'JA1260'
    password = '092902'
    sms_code = "%06d" % random.randint(0, 999999)
    content = '感谢注册91租机，验证码打死不要告诉别人哦！验证码：%s' % sms_code
    time = datetime.datetime.now()
    # 生成时间戳，格式为：月月日日时时分分秒秒
    time_stamp = time.strftime('%m%d%H%M%S')
    session_time_stamp = int(time.strftime('%y%m%d%H%M%S'))
    fixed_string = '00000000'
    # 报文密码为：（用户名 + 固定字符串 + 密码 + 时间戳）之后用md5加密
    combine_password = userid + fixed_string + password + time_stamp
    md5_password = hashlib.md5(combine_password.encode('UTF-8')).hexdigest()
    phone = request.GET.get('phone')
    urlencode_content = parse.quote(content, encoding='gb2312')
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
    res = re.search(phone_pat, phone)
    if res:
        query ={
            'userid': userid,
            'pwd': md5_password,
            'mobile': phone,
            'content': urlencode_content,
            'timestamp': time_stamp,
        }
        json_query = json.dumps(query)

        headers = {"Content-type": "application/json"}
        response = requests.post(send_url, data=json_query, headers=headers)
        if response.status_code == 200:
            data['success_message'] = '已发送'
            request.session['verify_code'] = sms_code
            request.session['phone'] = phone
            # request.session.set_expiry(60*60)
            request.session['time'] = session_time_stamp
            return JsonResponse(data)
        else:
            # Error handling code...
            print("Error: %s" % response.text)
            data['error_message'] = response.text
            return JsonResponse(data)
    else:
        data['error_message'] = '请输入正确手机号'
    return JsonResponse(data)


def signup_success(request):
    return render(request, 'blog/signup_success.html')


def merchants(request):
    merchants_list = Merchant.objects.order_by('id')
    context = {'merchants_list': merchants_list}
    return render(request, 'blog/merchants.html', context)


def merchant_detail(request, merchant_id):
    merchant = get_object_or_404(Merchant, pk=merchant_id)
    rows = find_merchant_user(merchant_id)
    context = {'merchant': merchant,
               'rows': rows,
               }
    return render(request, 'blog/merchant_detail.html', context)

