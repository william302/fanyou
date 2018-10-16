import oss2
import qrcode
from decouple import config
from django.conf import settings

access_key = config('ALIYUN_ACCESS_KEY')
access_key_secret = config('ALIYUN_ACCESS_SECRET')


def qrcode_upload(merchant_id):
    auth = oss2.Auth(access_key, access_key_secret)
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'rent-mall', connect_timeout=30)
    url = 'http://47.98.40.106/signup?dealer=%s' % merchant_id
    img = qrcode.make(url)
    image_path = settings.MEDIA_ROOT + '/qrcode/%s.png' % merchant_id
    img.save(image_path)

    object_name = 'merchants/qrcode/%s.png' % merchant_id
    result = bucket.put_object_from_file(object_name, image_path)
    aliyun_url = 'https://rent-mall.oss-cn-beijing.aliyuncs.com/merchants/qrcode/%s.png' % merchant_id
    print('http status: {0}'.format(result.status))
    print('request_id: {0}'.format(result.request_id))

    return aliyun_url
