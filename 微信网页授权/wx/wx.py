from flask import Flask,render_template,request
import util

app = Flask(__name__)

@app.route('/wx.html')
def wx():
    code = request.args.get('code','')
    state = request.args.get('state','')
    arg = util.get_web_token(code)
    print(arg['access_token'])
    print(arg['openid'])
    print(util.web_userinfo(arg['access_token'],arg['openid']))
    return render_template('wx.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
