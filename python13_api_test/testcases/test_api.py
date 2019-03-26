"""
@function：测试用例
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
class APITest(unittest.TestCase):
    do_excel = DoExcel(constants.case_file) # 读取cases.xlsx
    login_cases = do_excel.get_cases('login') # 指定读取login测试数据
    register_cases = do_excel.get_cases('register')
    request = Request() # 实例化对象

    mysql = MysqlUtil()
    sql = 'select max(mobilephone) from future.member'
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        self.max_mobilephone = self.mysql.fetch_one(self.sql)[0]
    def tearDown(self):
        pass

    @unittest.skip('调过不执行')
    @data(*login_cases)
    def test_login(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method,case.url,case.data)
        try:
            # 将返回结果和期望结果进行匹配
            self.assertEqual(case.expected,resp.text,'login error')
            # 一致就写入Excel的结果为Pass
            self.do_excel.write_result('login',case.id+1, resp.text, 'Pass')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            # 不一致就写入Excel的结果为Fail，并抛出异常
            self.do_excel.write_result('login',case.id+1,resp.text,'Fail')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    # mysql = MysqlUtil()
    # sql = 'select max(mobilephone) from future.member'
    # max_mobilephone = mysql.fetch_one(sql)[0]
    @data(*register_cases)
    def test_register(self, case):
        logger.info("开始执行第{0}用例".format(case.id))
        import json
        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == '${register_mobile}':
            data_dict['mobilephone'] = int(self.max_mobilephone) + 1  # 数据库中最大手机号+1
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_dict)
        try:
            # 将返回结果和期望结果进行匹配
            self.assertEqual(case.expected, resp.text, 'register error')
            # 一致就写入Excel的结果为Pass
            self.do_excel.write_result('register', case.id + 1, resp.text, 'Pass')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            # 不一致就写入Excel的结果为Fail，并抛出异常
            self.do_excel.write_result('register', case.id + 1, resp.text, 'Fail')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

