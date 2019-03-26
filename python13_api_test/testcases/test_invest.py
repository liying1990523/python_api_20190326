# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/26 11:22
@Author  : 
@function： 
"""
import unittest

from common.request import Request
from common.do_excel import DoExcel
from common import constants
from libext.ddtnew  import ddt,data
from common import context
from common.mysql import MysqlUtil
from common.context import Context
from common import logger

logger = logger.get_logger('cases')
@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(constants.case_file) # 读取cases.xlsx
    cases = do_excel.get_cases('invest1') # 指定读取invest测试数据

    @classmethod
    def setUpClass(cls): # 每个测试类里面去运行的操作放到类方法里面
        logger.debug('这是一个类方法\n')
        cls.request = Request()  # 实例化对象
        cls.mysql = MysqlUtil()
    @classmethod
    def tearDownClass(cls):
        cls.request.close() #关闭session
    def setUp(self): # 每个测试方法里面去运行的操作放到setUp里面
        logger.debug('这是一个对象方法')
        pass
    def tearDown(self):
        pass
    @data(*cases)
    def test_invest(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        # 从配置文件中读取替换
        data = context.replace(case.data)
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method,case.url,data)
        try:
            # 将返回结果和期望结果进行匹配
            self.assertEqual(case.expected,resp.json()['code'],'invest error')
            # 判断加标成功，如果加标成功，按照借款人ID去数据库查询最新标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context,'loan_member_id')
                sql = "SELECT Id FROM future.loan WHERE MemberID = '{0}' ORDER BY CreateTime DESC LIMIT 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0] #fetch_one方法返回的是一个元组，loan_id此时是int
                setattr(Context,'loan_id',str(loan_id)) # 后面要用正则的方法替换字符串，replace方法处理的是字符串
            # 一致就写入Excel的结果为Pass
            self.do_excel.write_result('invest1',case.id+1, resp.text, 'Pass')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            # 不一致就写入Excel的结果为Fail，并抛出异常
            self.do_excel.write_result('invest1',case.id+1,resp.text,'Fail')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e
