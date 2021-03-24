# coding:utf-8
# @Time: 2021/1/28 20:42
# @User: dengxin
# @Author: Ritter
import base64
import os

import requests



import  jenkins



#定义远程的jenkins master server 的url以及Port
jenkins_server_url = 'http://127.0.0.1:8080/'
#定义用户的userid 和 apitoken(在jenkins中生成)
user_id = 'ritter'
api_token = '123456' #测试服务器

server = jenkins.Jenkins(jenkins_server_url,username=user_id,password=api_token)
jobName1='API_Test'

joblog=server.get_build_console_output(jobName1,9)
print(joblog)

def get_build_state(server, name, build_number):
  '''

  :param name: job_name
  :param build_number: 最后1次构建序号
  :param:jenkins_server
  :return: 最后1次构建状态 pending,success,false,building
  '''
  build_state = None

  # 获取正在排队构建的job队列 即pending状态中的所有job,如果没有 pending状态的job即返回1个空列表
  queue_info = server.get_queue_info()

  if queue_info:
    for queue_job_info in queue_info:
      if queue_job_info['task']['name'] == name:
        # msg = 'pending期,排队构建中'
        build_state = 'pending'
  else:

    build_state = server.get_build_info(name, build_number)[
      'result'] # 构建结束 SUCCESS|FAILURE<class 'str'>  ABORTED <class 'str'> 构建中None None <class 'NoneType'>
  return build_state




url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2ed464df-50f4-4dc8-88a6-b1ad9a190940'
headers={
    'Content-Type': 'text/plain',
}
telephone_list=['15123274197']
data={
    "msgtype": "text",
    "text": {
        "content": """本次消息为调试活动,请大家忽略!
                    """,
        "mentioned_mobile_list":telephone_list,
    }
}

requests.post(url=url,headers=headers,json=data)