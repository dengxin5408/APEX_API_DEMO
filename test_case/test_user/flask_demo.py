# coding:utf-8
# @Time: 2021/1/26 14:19
# @User: dengxin
# @Author: Ritter
import random

from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)#Flask构造函数使用当前模块（__name __）的名称作为参数
app.config['JSON_AS_ASCII'] = False #支持返回中文
'''route()函数告诉应用程序哪个URL应该调用相关的函数,(rule,options)内rule填写与该函数绑定URL,
options 是要转发给基础Rule对象的参数列表(该函数绑定的请求方法)'''
@app.route("/api/user/reg/", methods=["POST"])
def reg():
    if not request.json or not 'name' in request.json or not 'password' in request.json:
        abort(404)
    res = [               #res是响应数据
              {
                "code": "100000",
                "msg": "成功",
                "data": {
                  "name": "李六",
                  "password": "e10adc3949ba59abbe56e057f20f883e"
                }
              },
              {
                "code": "100001",
                "msg": "失败，用户已存在",
                "data": {
                  "name": "李六",
                  "password": "e10adc3949ba59abbe56e057f20f883e"
                }
              },
              {
                "code": "100002",
                "msg": "失败，添加用户失败",
                "data": {
                  "name": "李六",
                  "password": "e10adc3949ba59abbe56e057f20f883e"
                }
              }
          ]

    return jsonify(random.choice(res))#使用jsonify 生成一个 JSON 的响应



if __name__ == "__main__":
    '''host 要监听的主机名(默认为127.0.0.1（localhost）),
    port 默认值为5000,debug 调试开关(设置为true，则提供调试信息) 
'''
    app.run(
        host = "127.0.0.1",
        port = 8989,
        debug = True
        )