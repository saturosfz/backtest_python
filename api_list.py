import time
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

try:
    import md5
    import urllib2
    from urllib import urlencode
except:
    import hashlib as md5
    import urllib.request as urllib2
    from urllib.parse import urlencode

accessKey = '64371b052b4c217baf12ce60d9050faf'
secretKey = 'def62b48ff97006ab30f777547479f5a'

def api(method, *args):
    d = {
        'version': '1.0',
        'access_key': accessKey,
        'method': method,
        'args': json.dumps(list(args)),
        'nonce': int(time.time() * 1000),
        }

    d['sign'] = md5.md5(('%s|%s|%s|%d|%s' % (d['version'], d['method'], d['args'], d['nonce'], secretKey)).encode('utf-8')).hexdigest()
    # 注意： urllib2.urlopen 函数，超时问题，可以设置超时时间，urllib2.urlopen('https://www.fmz.cn/api/v1', urlencode(d).encode('utf-8'), timeout=10) 设置超时 10秒
    return json.loads(urllib2.urlopen('https://www.fmz.cn/api/v1', urlencode(d).encode('utf-8')).read().decode('utf-8'))

exchanges = api('GetExchangeList')['data']['result']['exchanges']
print([ex['eid'] for ex in exchanges])
print(api('GetExchangeList'))
