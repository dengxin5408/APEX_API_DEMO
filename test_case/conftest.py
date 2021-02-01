import pytest

from config.conf import test_zy_url, test_zy_login_data
from tools.api import request_tool
import json
                                                            
@pytest.fixture(scope='session')  #fixture打下标签作为公共登录拿到token
def public_token():

    url=test_zy_url
    req=test_zy_login_data
    resp=request_tool.post_json(url,json=req)
    resp_json=json.loads(resp.text)
    token=resp_json['data']['token']
    # 取出登录后token,存入变量
    return token


