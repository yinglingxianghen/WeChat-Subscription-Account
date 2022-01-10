import util.wx_util as wx_util

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
                       "value":"中奖了",
                       "color":"blue"
                   },
                   "keyword2": {
                       "value":"一等奖",
                       "color":"green"
                   },
                   "keyword3": {
                       "value":"鼠标",
                       "color":"red"
                   },
                   "keyword4":{
                       "value":"很快就会邮递给你",
                       "color":"blue"
                   },
                   "remark":{
                       "value":"哈哈哈哈！",
                       "color":"green"
                   }
           }
       }
''' % (openid,'5R-zLa_T5xt7Qp9tNI51EaL_ctWqTkq8iMmnx7Ice1A')).encode('utf-8')

print(wx_util.send_template(arg))