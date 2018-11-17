from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from wechatpy import parse_message, WeChatClient
from wechatpy.replies import TextReply, ArticlesReply, ImageReply
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from wechatpy.exceptions import WeChatClientException


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
                    'title': '91租机人气之星投票大赛',
                    'description': '',
                    'image': 'https://fanyou-static.oss-cn-hangzhou.aliyuncs.com/images/basketball-bg.jpg',
                    'url': 'https://www.fanyoutech.com/basketball/'
                })
                r_xml = reply.render()
                return HttpResponse(r_xml)
            if msg.content == '名字':
                client = WeChatClient(app_id, secret)
                user_id = msg.source
                try:
                    user = client.user.get('dd')
                except Exception as e:
                    print(e)

                reply = TextReply(content='你是', message=msg)
                r_xml = reply.render()
                return HttpResponse(r_xml)
            else:
                content = "感谢反馈，我们已经收到了你的留言"
                reply = TextReply(content=content, message=msg)
                r_xml = reply.render()
                return HttpResponse(r_xml)
        if msg.type == 'event':
            if msg.event == 'subscribe':
                reply = TextReply(content='谢谢关注91租机，更多详情请下载【91租机】APP', message=msg)
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
        else:
            content = "感谢反馈，我们已经收到了你的留言"
            reply = TextReply(content=content, message=msg)
            r_xml = reply.render()
            return HttpResponse(r_xml)



