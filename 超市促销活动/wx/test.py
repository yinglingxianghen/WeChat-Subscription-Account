import http.client

import json

appid = 'wx62c7bdcd5756636b'
appsecret = '7851cf7a7ab7c13f0a95ff765b429536'

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

openid = 'oTKX2s89zdVbY8YfIyU8eAMePQp8'

arg = ('''
{
           "touser":"%s",
           "template_id":"%s",          
           "data":{
                   "first": {
                       "value":"九宝2326321088",
                       "color":"red"
                   },
                   "keyword1":{
                       "value":"巧克力",
                       "color":"blue"
                   },
                   "keyword2": {
                       "value":"39.8元",
                       "color":"green"
                   },
                   "keyword3": {
                       "value":"2014年9月22日",
                       "color":"red"
                   },
                   "keyword4":{
                       "value":"巧克力",
                       "color":"#173177"
                   },
                   "remark":{
                       "value":"欢迎再次购买！",
                       "color":"#173177"
                   }
           }
       }
''' % (openid,'5R-zLa_T5xt7Qp9tNI51EaL_ctWqTkq8iMmnx7Ice1A')).encode('utf-8')

print(send_template(arg))