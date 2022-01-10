from flask import Flask,request
import util.wx_util as wx_util

app = Flask(__name__)


@app.route('/wx_interface',methods=['GET','POST'])
def wx_interface():
    if 'GET' == request.method:
        return wx_util.wx_validate(request)
    if 'POST' == request.method:
        request_str = str(request.data,'utf-8')
        read_dict = wx_util.xmlTodict(request_str)
        if 'text' == read_dict['xml']['MsgType']:
            Content = read_dict['xml']['Content']
            #这是活动的关键词
            #第一个发来'饿了就回家吃饭'的粉丝，将得到xxxxxxx
            if '饿了就回家吃饭' == Content:
                #判断是第一个粉丝
                #将粉丝的信息写到数据库
                #返回中奖提示
                return wx_util.get_text_return(read_dict,'中奖了，稍后会有客服和你联系的，。。。。')
            else:
                return wx_util.get_text_return(read_dict, '关键字不对，不能中奖')
        else:
            return ''




        return ''
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
