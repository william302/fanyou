import oss2


# print(result.__str__())
# print('http status: {0}'.format(result.status))
# print('request_id: {0}'.format(result.request_id))
# print('ETag: {0}'.format(result.etag))
# print('date: {0}'.format(result.headers['date']))

def business_license_upload(instance, filename):
    auth = oss2.Auth('LTAIbnw6ov01skHL', 'Ya2aclHY1GrRwgy07HdFqGK75H4Hqe')
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'rent-mall', connect_timeout=30)
    object_name = 'merchants/%s' % filename
    result = bucket.put_object_from_file(object_name, instance)
    print('http status: {0}'.format(result.status))
    print('request_id: {0}'.format(result.request_id))
    print('ETag: {0}'.format(result.etag))
    print('date: {0}'.format(result.headers['date']))