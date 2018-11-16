from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from wechatpy import parse_message, WeChatClient
from wechatpy.replies import TextReply, ArticlesReply, ImageReply
from django.views.decorators.csrf import csrf_exempt
from decouple import config


app_id = config('WECHAT_APPID')
secret = config('WECHAT_SECRET')


@csrf_exempt
def index(request):
    if request.method == 'GET':
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
    else:
        xml = request.body
        msg = parse_message(xml)
        if msg.type == 'text':
            if msg.content == '投票':
                reply = ArticlesReply(message=msg)
                reply.add_article({
                    'title': '91租机篮球活动',
                    'description': 'fdfdfefdsfdsvsffefdsvsdsfefdsddsdc',
                    'image': 'https://fanyou-static.oss-cn-hangzhou.aliyuncs.com/images/bg-cta.jpg',
                    'url': 'https://www.fanyoutech.com/basketball/'
                })
                r_xml = reply.render()
                return HttpResponse(r_xml)
            if msg.content == '名字':
                client = WeChatClient(app_id, secret)
                user_id = msg.source
                print(user_id)
                user = client.user.get(user_id)
                print(user)
                reply = TextReply(content='你是'+user.get('nickname'), message=msg)
                r_xml = reply.render()
                return HttpResponse(r_xml)
            else:
                content = "感谢反馈，我们已经收到了你的留言"
                try:
                    reply = TextReply(content=content, message=msg)
                    r_xml = reply.render()
                    return HttpResponse(r_xml)
                except Exception as e:
                    pass
        if msg.type == 'event':
            if msg.event == 'subscribe':
                reply = TextReply(content='谢谢关注91租机', message=msg)
                r_xml = reply.render()
                return HttpResponse(r_xml)
            if msg.event == 'unsubscribe':
                reply = TextReply(content='老乡别走', message=msg)
                r_xml = reply.render()
                return HttpResponse(r_xml)
        if msg.type == 'image':
            reply = ImageReply(media_id=msg.media_id, message=msg)
            r_xml = reply.render()
            return HttpResponse(r_xml)


