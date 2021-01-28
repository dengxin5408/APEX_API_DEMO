
import pymssql



class SqlServerDataBase:

        def __init__(self, host, username, pwd, databaseName):
        #创建构造函数
                self.serverhost = host
                self.username = username
                self.pwd = pwd
                self.databaseName = databaseName

        def connects(self):
            #数据库连接
                self.sqlserver_conn = pymssql.connect(host=self.serverhost, databaseName=self.databaseName, username=self.username,pwd=self.pwd,port=1433,charset='utf-8',as_dict=True)
                cur = self.sqlserver_conn.conn.cursor()
                if not cur:
                    raise (NameError,'连接数据库失败')
                else :
                    return cur

if __name__ == '__main__':
            sqlserver_db = SqlServerDataBase('192.168.100.212', 'gasweb', 'gaswebgasgoo2015', '智配test')
            print(sqlserver_db,'pass')