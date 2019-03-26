# -*- coding:utf-8 -*-
"""
@function：注册的测试用例
"""
import unittest

from common.request import Request
from common.do_excel import DoExcel
from common import constants
from libext.ddtnew  import ddt,data
from common.mysql import MysqlUtil
from common import logger

logger = logger.get_logger('cases')
@ddt
class RegisterTest(unittest.TestCase):
    do_excel = DoExcel(constants.case_file)  # 读取cases.xlsx
    register_cases = do_excel.get_cases('register')
    request = Request()  # 实例化对象

    mysql = MysqlUtil(return_dict= True)
    sql = 'select max(mobilephone) as max_mobilephone from future.member'

    def setUp(self):
        self.max_mobilephone = self.mysql.fetch_one(self.sql)['max_mobilephone']

    @data(*register_cases)
    def test_register(self, case):
        logger.info("开始执行第{0}用例".format(case.id))
        import json
        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == '${register_mobile}':
            data_dict['mobilephone'] = int(self.max_mobilephone) + 1  # 数据库中最大手机号+1
        if 'regname' in data_dict.keys():
            regname = data_dict['regname']
        else:
            regname = None
        # print(regname)
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_dict)
        # print(resp.json())
        try:
            # 将返回结果和期望结果进行匹配
            self.assertEqual(case.expected, resp.text, 'register error')
            # 一致就写入Excel的结果为Pass
            self.do_excel.write_result('register', case.id + 1, resp.text, 'Pass')
            if resp.json()['msg'] == '注册成功':
                sql = "select * from future.member where mobilephone = '{0}'".format(data_dict['mobilephone'])
                result = self.mysql.fetch_all(sql)
                # 首先判断是否有成功插入数据
                self.assertEqual(1, len(result), '注册成功时，仅在数据库中插入一条数据')
                # 判断注册成功余额应该是0
                self.assertEqual(0, result[0]['LeaveAmount'], '注册成功后，初始余额应该是0')
                # 判断regname
                if regname:
                    self.assertEqual(regname, result[0]['RegName'])
                else:
                    self.assertEqual('小蜜蜂', result[0]['RegName'])
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            # 不一致就写入Excel的结果为Fail，并抛出异常
            self.do_excel.write_result('register', case.id + 1, resp.text, 'Fail')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()
