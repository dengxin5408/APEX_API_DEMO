import pytest

from tools.api import request_tool


'''id2=['正确数据',
     '用户名错误',
     '密码错误']
# case的标题,参数存入ids中
cases=[('xiewu1','qYFn2Y4a',2000),
       ('xiewu','qYFn2Y4a',9999),
       ('xiewu1','qYFn2Y4',9999)]
# []里为请求参数,()里为一个完整的case,和预期结果
@pytest.mark.parametrize('name,pwd,assertion',cases,ids=id2)
def test_login(name,pwd,assertion):
    url='http://www.guoyasoft.com:8084/login'
    req={
      "pwd": pwd,
      "userName": name
    }
    resp=request_tool.post_json(url,json=req)
    print(resp)
    resp_json = resp.json()
    code=resp_json['code']
    print(code)
    data=resp_json['data']
    assert code == assertion
'''
# coding:utf-8
# @Time: ${DATE} ${TIME}
# @User: ${USER}
# @Author: Ritter
import pytest
#第一步pip install flaky
#max_runs=1 第一次失败后运行1次,min_passes=1.最少执行一次成功才算通过
#reruns=5, reruns_delay=2：最多失败重跑5次 & 如果失败则延迟1秒后重跑（可以不传）
@pytest.mark.flaky(max_runs=1, min_passes=1)
def test01():
    a = 1
    b = 2
    assert a == b
    print("失败重跑")
