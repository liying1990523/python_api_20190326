# -*- coding:utf-8 -*-
"""
@function：数据库操作
"""
import pymysql
from common.config import ReadConfig

class MysqlUtil:
    def __init__(self,return_dict = False):
        config = ReadConfig()
        host = config.get('db','host')
        user = config.get('db','user')
        password = config.get('db','password')
        port = config.getint('db','port')
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port,charset="utf8")
        if return_dict:
            self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor) # 指定每行数据以字典的形式返回
        else:
            self.cursor = self.mysql.cursor() # 此语句放在初始化里面，表示多次查询建立一个查询页面
                                              # 指定每行数据以元祖的形式返回

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone() # 若用self.cursor = self.mysql.cursor()  返回元祖(0,) 取值用result[0]
                        #若使用self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor) 返回字典{} 取值用result[key]
        return result

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()  # 若用self.cursor = self.mysql.cursor()  返回元祖嵌套元组((),(),())
                            #若使用self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor) 返回列表嵌套字典[{},{}]
        return results

    def close(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    # mysql = MysqlUtil()
    # sql = 'select max(mobilephone) from future.member'
    # result = mysql.fetch_one(sql)
    # print(result)
    # print(result[0])
    # mysql.close()

    mysql = MysqlUtil(return_dict=True)
    # mysql = MysqlUtil()
    sql = "select * from future.member limit 10"
    # results = mysql.fetch_all(sql)  # 返回的是列表里面放字典
    results = mysql.fetch_one(sql)
    print(results)
    # print(type(results[0]))
    print(type(results))
    print(type(results['RegTime']),results['RegTime'])
    # for result in results:
    #     print(type(result),result)
    mysql.close()
