# coding:utf-8
# @Time: 2021/1/28 19:46
# @User: dengxin
# @Author: Ritter

import requests
import json
import urllib.request
import urllib.error
import time


# 获取构建结果

def getResult():
    fname = pathGitLab
    with open(fname, 'rb') as f:  # 打开文件

        first_line = f.readline()  # 读第一行
        # print (first_line)
        off = -50  # 设置偏移量

        while True:

            f.seek(off, 2)  # seek(off, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)

            lines = f.readlines()  # 读取文件指针范围内所有行
            # print (lines)

            if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的

                last_line = lines[-1]  # 取最后一行
                print(last_line)

                break

            off *= 2

        if 'FAILURE' in last_line.decode():
            return 1

        # else:

        #     return 0


# 获取下一次构建的Number和当前构建的number

def getNextNumber():
    f = open(r'C:\Program Files (x86)\Jenkins\jobs\Developer\nextBuildNumber', 'r')

    currentNumber = int(f.read()) - 1

    return currentNumber


# 网络模块，用于企业微信发送信息

def jenkins(result):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2ed464df-50f4-4dc8-88a6-b1ad9a190940'
    # 企业微信机器人的webhook

    if result == 1:
        con = {"msgtype": "text",
               "text": {"content": "站点构建提醒\r\n构建站点:Developer\r\n构建结果:FAILURE\r\n构建失败，请您检查代码并重新构建，谢谢"}, }
    # else :
    #     con={"msgtype": "text","text": {"content": "developer构建结果：构建失败，请检查代码后重试！"},}

    jd = json.dumps(con).encode('utf-8')

    req = urllib.request.Request(url, jd)

    req.add_header('Content-Type', 'application/json')

    response = urllib.request.urlopen(req)


if __name__ == '__main__':
    jobCurrentNumber = getNextNumber()  # 获取当前构建number
    # print (jobCurrentNumber)
    # myDict=getDict()#获取同事所有联系方式
    # 获取当前构建的目录比如D:\Jenkins\jobs\gk_check\builds\153,
    path = "C:\\Program Files (x86)\\Jenkins\\jobs\\Developer\\builds\\" + str(jobCurrentNumber) + "\\"

    pathGitLab = path + "log"  # 获取svn版本和id信息的文件路径

    pathAuthor = path + "changelog.xml"  # 获取递交者信息的文件路径

    result = getResult()  # 读取构建结果
    # print (result)

    jenkins(result)  # 最后执行函数
    getResult()
