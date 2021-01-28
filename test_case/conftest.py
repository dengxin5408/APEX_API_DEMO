import pytest

from tools.api import request_tool
from config import conf
from test_case.test_user import test_sign
@pytest.fixture(scope='session')
def public_token():
    url = conf.test_zy_url
    headers =conf.headers
    req =conf.test_zy_login_data
    resp = request_tool.post_json(url=url, json=req,headers=headers)
    token = resp.json()['data']['token']
    print(token)



'''通过fixture()将参数传递给所有test_方法,在执行中所有case中共享一个session,从第一个case开始,最后一个caes结束的时候session结束'''

'''def test_login():
    url='http://www.guoyasoft.com:8084/login'
    req={
      "pwd":test_sign.test_sign().pwd,
      "userName": test_sign.test_sign().username
    }
    resp=request_tool.post_json(url,json=req)
    print(resp)
    resp_json = resp.json()
    code=resp_json['code']
    print(code)
    data=resp_json['data']
    assert code == 2000 and data!=None
    return resp_json()['data']['token']'''