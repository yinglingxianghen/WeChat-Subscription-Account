import urllib.request
import http.client
import json
def get_redirect_uri(redirect_uri,state):
    return 'https://open.weixin.qq.com/connect/oauth2/authorize?' \
           'appid=%s&' \
           'redirect_uri=%s&' \
           'response_type=code&' \
           'scope=%s&' \
           'state=%s#wechat_redirect' % ('wx62c7bdcd5756636b',
                                            urllib.request.quote(redirect_uri),
                                            'snsapi_base',
                                            state)

def get_web_token(arg):
    conn = http.client.HTTPSConnection('api.weixin.qq.com')
    conn.request('GET','/sns/oauth2/access_token?'
                       'appid=%s&'
                       'secret=%s&'
                       'code=%s&'
                       'grant_type=authorization_code' % (
                        'wx62c7bdcd5756636b',
                        '7851cf7a7ab7c13f0a95ff765b429536',
                        arg))
    response = conn.getresponse()
    text = str(response.readline(),'utf-8')

    conn.close()

    return json.loads(text)

def web_userinfo(access_token,openid):
    conn = http.client.HTTPSConnection('api.weixin.qq.com')
    request = conn.request('GET','/sns/userinfo?access_token=%s'
                                     '&openid=%s&lang=zh_CN' % (
        access_token,openid
    ))
    response = conn.getresponse()
    text = str(response.readline(), 'utf-8')
    conn.close()
    return json.loads(text)