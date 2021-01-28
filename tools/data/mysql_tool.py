
import pymysql
from pymssql import IntegrityError


class DataBaseHandle(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self, host, username, password, database, port):
     try:

        '''初始化数据库信息并创建数据库连接'''
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, self.port, charset='utf8',
                                      cursorclass=pymysql.cursors.DictCursor)

        '''DictCursor的作用是将查询的返回值会变成字典格式,取到字段名和字段值
        DictCursor的这个功能是继承于CursorDictRowsMixIn，
         这个MixIn提供了3个额外的方法: fetchoneDict、fetchmanyDict、fetchallDict
         '''
        self.cur = self.db.cursor()
     except Exception as ConnectError:
         print('连接错误:请检查下列请求参数',ConnectError)



    # 这里是为了实例化对象,一开始就创立连接,不用单独定义方法



    def delete(self,tablename,cond_dict):

       try:
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    v = "\'" + v + "\'"
                consql = consql  + k + '=' + v

        sql = "DELETE FROM %s where%s" % (tablename,consql)
        print(sql)
        self.executeCommit(sql)
        sql_seclect =  'SELECT COUNT(*)  FROM ' + tablename
        self.db.ping(reconnect=True)
        result = self.showDb(sql_seclect)
        return '删除后查询结果: %s' % result
       except Exception:
           self.db.rollback()

       finally:
           self.cur.close()



    def showDb(self,sql):

        resp={}
        resp['status']='0000'
        resp['error']=None
        resp['result']=None
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            content = self.cursor.fetchall()  # 返回所有记录列表

            # 获取表头
            labels = self.cursor.description
            labels = ['name']

            table_data = {}
            table_data['content'] = content
            table_data['labels'] = labels
            resp['result']=table_data
            return resp
        except Exception as e:
            print(e)
            resp['status'] = '0001'
            resp['error'] = e
            return resp
        finally:
            self.cursor.close()


    def executeCommit(self, sql):
        """执行数据库sql语句，针对更新,删除,事务等操作失败时回滚

        """
        try:

            self.db.ping(reconnect=True)
            self.cur.execute(sql)
            self.db.commit()
        except pymysql.Error as e:
            self.db.rollback()
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])

            return error
        finally:
            self.db.close()


    def insert(self,tablename,params ):
      global sql_insert
      try:
        key = []
        value = []
        for tmpkey, tmpvalue in params.items():
            key.append(tmpkey)
            if tmpvalue.isdigit():
                value.append(tmpvalue)
            else:
                value.append("\'" + tmpvalue + "\'")
            '''判断tmpvalue包含数字,添加进value.反之给每次遍历的tmpvalue追加双引号'''
        attrs_sql = '(' + ','.join(key) + ')'
        values_sql = ' values(' + ','.join(value) + ')'
        sql = 'INSERT INTO %s' % tablename
        sql_insert = sql + attrs_sql + values_sql
        self.executeCommit(sql_insert)
        print('成功执行:' + sql_insert)
      except Exception as error :
          print(error,'error:KEY重复或SQL语句有误,请检查!-->>',sql_insert)
      finally:
          self.db.close()

    def update(self,tablename, attrs_dict, cond_dict):
        """更新数据
                   args：
                       tablename  ：表名字
                       attrs_dict  ：更新属性键值对字典
                       cond_dict  ：更新条件字典
                   example：
                       params = {"name" : "caixinglong", "age" : "38"}
                       cond_dict = {"name" : "liuqiao", "age" : "18"}
                       mydb.update(table, params, cond_dict)
        """
        attrs_list = []
        consql = ' '
        for tmpkey, tmpvalue in attrs_dict.items():
            attrs_list.append(tmpkey   + "=" + "\'" + tmpvalue + "\'")
        attrs_sql = ",".join(attrs_list)
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    v = "\'" + v + "\'"
                consql = consql +  k  + '=' + v
        sql = "UPDATE %s SET %s where%s" % (tablename, attrs_sql, consql)
        print('成功执行:'+sql)
        self.executeCommit(sql)
        sql_quary = 'SELECT *'  + ' FROM ' + tablename + ' where '+attrs_sql
        self.db.ping(reconnect=True)
        '''检查连接是否关闭,关闭后重新连接'''
        returned_value  = self.showDb(sql_quary)
        return returned_value

    def select(self, table, filed, value):
        sql = "SELECT * FROM {table} WHERE {filed} = '{value}'".format(table=table, filed=filed, value=value)

        result = self.showDb(sql)
        print(sql)
        return result



if __name__ == '__main__':

    DbHandle = DataBaseHandle('10.25.21.68','market_test','2aEcjc%Ew4h','apex_test_market_center',3306)



    w = DbHandle.select(table = 'member_zy',filed='nickname',value= 'Ritter老邓')





    #f = DbHandle.insert(tablename='apex_test_market_center.member_sys',params={'id':'22','account':'229s0','password':'2239f0','create_time':'2021-01-12 15:14:36','update_time':'2021-01-12 15:14:36','del_flag':'9','create_by':'99',})
    #s = DbHandle.update(tablename='apex_test_market_center.member_sys', attrs_dict={'account':'9990'},cond_dict={'account':'229s0'})

    #E = DbHandle.delete(tablename='apex_test_market_center.member_sys',cond_dict={'account':'2290'})
    print(w)
