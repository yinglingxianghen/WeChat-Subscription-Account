import http.client
import json
import hashlib

def get_accesstoken():
    # 得到conn
    conn = http.client.HTTPSConnection("api.weixin.qq.com")
    # get方式访问
    conn.request("GET", "/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % ('wx62c7bdcd5756636b', '7851cf7a7ab7c13f0a95ff765b429536'))
    response = conn.getresponse()
    # 获取相应结果
    text = str(response.readline(), 'utf-8')
    conn.close()

    return json.loads(text)

def get_jsapi_ticket():
    # 得到conn
    conn = http.client.HTTPSConnection("api.weixin.qq.com")
    # get方式访问
    conn.request("GET", "/cgi-bin/ticket/getticket?access_token=%s&type=jsapi" % get_accesstoken()['access_token'])
    response = conn.getresponse()
    # 获取相应结果
    text = str(response.readline(), 'utf-8')
    conn.close()

    return json.loads(text)

def get_signature(noncestr,timestamp,url):
    jsapi_ticket = get_jsapi_ticket()['ticket']
    str = 'jsapi_ticket=%s&noncestr=%s&timestamp=%s&url=%s' % (
        jsapi_ticket,
        noncestr,
        timestamp,
        url
    )
    print(str)
    return hashlib.sha1(bytes(str,'utf-8')).hexdigest()
