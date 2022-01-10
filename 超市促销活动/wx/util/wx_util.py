import hashlib
import xmltodict
import http.client
import json

appid = 'wx62c7bdcd5756636b'
appsecret = '7851cf7a7ab7c13f0a95ff765b429536'

def wx_validate(request):
    token = 'jiubao'
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    list = [token, timestamp, nonce]
    list.sort()
    _signature = hashlib.sha1(bytes(list[0] + list[1] + list[2], 'utf-8')).hexdigest()
    if _signature == signature:
        return echostr
    else:
        return ''

def xmlTodict(arg):
    return xmltodict.parse(arg)

def get_text_return(arg,str):
    return '<xml>' \
           '<ToUserName><![CDATA[%s]]></ToUserName>' \
           '<FromUserName><![CDATA[%s]]></FromUserName>' \
           '<CreateTime>12345678</CreateTime>' \
           '<MsgType><![CDATA[text]]></MsgType>' \
           '<Content><![CDATA[%s]]></Content>' \
           '</xml>' % (arg['xml']['FromUserName'],arg['xml']['ToUserName'],str)

def get_accessToken():
    conn = http.client.HTTPSConnection('api.weixin.qq.com')
    conn.request('GET','/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid,appsecret))
    response = conn.getresponse()
    text = str(response.readline() , 'utf-8')
    conn.close()
    return json.loads(text)

def create_menu(arg):
    conn = http.client.HTTPSConnection('api.weixin.qq.com')
    conn.request('POST','/cgi-bin/menu/create?access_token=%s' % get_accessToken()['access_token'],arg)
    response = conn.getresponse()
    text = str(response.readline(),'utf-8')
    print(text)

def send_server(arg):
    conn = http.client.HTTPSConnection('api.weixin.qq.com')
    conn.request('POST','/cgi-bin/message/custom/send?access_token=%s' % get_accessToken()['access_token'],arg)
    response = conn.getresponse()
    text = str(response.readline(),'utf-8')
    print(text)

def send_template(arg):
    conn = http.client.HTTPSConnection('api.weixin.qq.com')
    conn.request('POST','/cgi-bin/message/template/send?access_token=%s' % get_accessToken()['access_token'] , arg)
    response = conn.getresponse()
    text = str(response.readline(),'utf-8')
    print(text)