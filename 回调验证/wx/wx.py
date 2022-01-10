from flask import Flask,request
import hashlib
import util.util as util

app = Flask(__name__)


@app.route('/wx_interface', methods=['GET', 'POST'])
def wx_interface():
    if request.method=='GET':
        token = 'jiubao'
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')

        list = [token,timestamp,nonce]
        list.sort()
        _signature = hashlib.sha1(bytes(list[0]+list[1]+list[2],'utf-8')).hexdigest()
        if _signature == signature:
            return echostr
        else:
            return ''
    if request.method == 'POST':
        request_str = str(request.data,'utf-8')
        print(request_str)

        read_dict = util.xmlTodict(request_str)

        if 'text' == read_dict['xml']['MsgType']:
            return '<xml>' \
                   '<ToUserName><![CDATA[%s]]></ToUserName>' \
                   '<FromUserName><![CDATA[%s]]></FromUserName>' \
                   '<CreateTime>12345678</CreateTime>' \
                   '<MsgType><![CDATA[text]]></MsgType>' \
                   '<Content><![CDATA[%s]]></Content></xml>' % \
                   (read_dict['xml']['FromUserName'],read_dict['xml']['ToUserName'],'server  '+read_dict['xml']['Content'])
        elif 'image' == read_dict['xml']['MsgType']:
            print('这是image')
        elif 'voice' == read_dict['xml']['MsgType']:
            print('这是voice')
        elif 'video'==read_dict['xml']['MsgType']:
            print('这是video')
        elif 'shortvideo'==read_dict['xml']['MsgType']:
            print('这是shortvideo')
        elif 'location'==read_dict['xml']['MsgType']:
            print('这是location')
        else:
            return ''
        return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
