import oss2
import qrcode
from decouple import config
from django.conf import settings
from PIL import Image

access_key = config('ALIYUN_ACCESS_KEY')
access_key_secret = config('ALIYUN_ACCESS_SECRET')
auth = oss2.Auth(access_key, access_key_secret)
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'rent-mall', connect_timeout=30)


def qrcode_upload(merchant_id):
    auth = oss2.Auth(access_key, access_key_secret)
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'rent-mall', connect_timeout=30)
    url = 'http://47.98.40.106/signup?dealer=%s' % merchant_id

    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    icon = Image.open(settings.MEDIA_ROOT + "/favicon-96x96.png")  # 这里是二维码中心的图片

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    image_path = settings.MEDIA_ROOT + '/qrcode/%s.png' % merchant_id
    img.save(image_path)

    oss_path = config('ALIYUN_OSS_PATH')
    object_name = oss_path % merchant_id
    result = bucket.put_object_from_file(object_name, image_path)

    http_oss_path = config('HTTP_OSS_PATH')
    aliyun_url = http_oss_path % merchant_id
    print('http status: {0}'.format(result.status))
    print('request_id: {0}'.format(result.request_id))
    print('sss')

    return aliyun_url

def bussiness_license_upload(image_path):
    image_path = settings.MEDIA_ROOT + image_path
    result = bucket.put_object_from_file('merchants/')