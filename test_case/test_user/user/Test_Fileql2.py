# coding:utf-8
# @Time: 2021/1/28 20:48
# @User: dengxin
# @Author: Ritter
import os,datetime
import pytest




'''def fileql( *args,**kwargs):
 ds = list(os.walk(*args,**kwargs)) #获得所有文件夹的信息列表
 delta = datetime.timedelta(days=7) #设定365天前的文件为过期
 now = datetime.datetime.now() #获取当前时间
 for d in ds: #遍历该列表
  os.chdir(d[0]) #进入本级路径，防止找不到文件而报错
  if d[2] != []: #如果该路径下有文件
    for x in d[2]: #遍历这些文件
      ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #获取文件创建时间
      if ctime < (now-delta): #若创建于delta天前
       os.remove(x) #则删掉'''



ids=['html_path','xml_path']
pathlist=['C:/softwoer/dev/API_test/reports/reports_html','C:/softwoer/dev/API_test/reports/xml']
@pytest.mark.parametrize('ql_path',pathlist,ids=ids)
def test_fileql2(ql_path):
 try:
    ds = list(os.walk(ql_path))  # 获得所有文件夹的信息列表
    dsr = ds[::-1]  # 反转该列表，从最底层的文件夹开始清算
    for d in dsr:  # 遍历该列表
        print(d)  # 打印出列表项，观察规律
        if d[2] != []:  # 如果该路径下有文件
            for x in d[2]:  # 先将文件清理干净
                os.remove(os.path.join(d[0], x))
        print('------------------启动第一次清除')
    for d in dsr:  # 再次遍历该列表
        if d[1] != []:  # 如果该路径下有子文件夹
            for y in d[1]:  # 将子文件夹清理干净
                os.rmdir(os.path.join(d[0], y))
        print('------------------启动第二次清除')

 except EOFError:

     print('读取文件失败',ql_path)

 finally:
     print(format(ql_path),':历史数据已清除')

