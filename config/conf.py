GY_EMAIL_QA = {
    'on_off': 'on',  # 邮件是否发生，on发送，off不发送
    'mail_host': 'smtp.126.com',  # 设置服务器
    'mail_user': 'wuling1105@126.com',  # 用户名
    'mail_pass': '126shouquanma',  # 口令
    'sender': 'wuling1105@126.com',
    'mail_port': 25,
    'receivers': ['wuling@guoyasoft.com', 'wuling1105@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
}
headers = {"Content-Type": "application/json;charset=UTF-8 ",
           "Origin": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn"
    , "Referer": "https: // apex - test - zhuoyue - mini - admin.chinapex.com.cn/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    , "Accept": "application/json,text/plain,*/*", "Accept-Encoding": "gzip,deflate,br",
           "Accept-Language": "zh-CN,zh;q=0.9"
           }

req = {
    "password": 'zhuoyue',
    "username": '123456'
}
# 卓越转介绍test环境 login url
test_zy_url = 'https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login'
test_zy_login_data = {
        "password": "123456",
        "username": "zhuoyue"
    }
#转介绍用户查询
test_zjs_userquery_url='https://zjs.zytest.net/service/manage/api/zy/pageList'
test_zjs_userquery_data= {"pageNum": 1,"pageSize": 10,"ppId": "", "phone": "","nickName": "Ritter老邓"}
