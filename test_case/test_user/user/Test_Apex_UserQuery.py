# -*- coding: utf-8 -*-
# @Time: 2021/2/1 10:39
# @User: dengxin
# @Author: Ritter



from tools.data.mysql_tool import DataBaseHandle
from config import conf
from tools.api import request_tool


def test_post_json(public_token):

    data = conf.test_zjs_userquery_data #data是请求体
    hearders=  {'x-token':public_token   }#hearders是请求头,public_token是公共参数
    rq =  request_tool.post_json(url= conf.test_zjs_userquery_url,headers=hearders,json=data)#将POST请求作为JSON串发送
    code = rq.json()['code']
    ipone =rq.json()['data']['list'][0]['phoneNumber']#获取response需校验字段
    if code=='200'and ipone == '15123274197':#第一次校验code和手机号
        DbHandle = DataBaseHandle('10.25.21.68', 'market_test', '2aEcjc%Ew4h', 'apex_test_market_center', 3306)#连接mysqldb
        s = DbHandle.select(table = 'member_zy',filed='nickname',value= 'Ritter老邓')
        select_result=s['result']['content'][0]['phone_number']
        assert  select_result == '15123274197'#第二次查询数据库校验手机号
        print('PASS')
    else:
        print('FALSE')