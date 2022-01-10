from flask import Flask,render_template,request
import time
import util

app = Flask(__name__)

@app.route('/wx')
def wx():
    appId = 'wx62c7bdcd5756636b'
    timestamp = str(int(time.time()))
    nonceStr = 'jiubao2326321088'
    arg = {'appId':appId,
            'timestamp':timestamp,
            'nonceStr':nonceStr,
           'signature':util.get_signature(nonceStr,timestamp,'http://huashengke0.iok.la/wx')
    }
    return render_template('wx.html',arg=arg)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
