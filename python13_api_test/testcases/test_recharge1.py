"""
@function：充值的测试用例 ，利用resp.cookies
"""
import unittest

from common.do_excel import DoExcel
from common import constants
from libext.ddtnew  import ddt,data
import json
import requests
from common import logger

logger = logger.get_logger('cases')
@ddt
class LoginTest(unittest.TestCase):
    do_excel = DoExcel(constants.recharge_cases) # 读取cases.xlsx
    cases = do_excel.get_cases('recharge') # 指定读取login测试数据

    @classmethod
    def setUpClass(cls): # 每个测试类里面去运行的操作放到类方法里面
        logger.debug('这是一个类方法\n')
        # cls.login_data = {'mobilephone': '15810447656', 'pwd': '123456'}
        # cls.login_resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=cls.login_data)
        # print(cls.login_resp.text)

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self): # 每个测试方法里面去运行的操作放到setUp里面
        logger.debug('这是一个对象方法')
        self.login_data = {'mobilephone': '15810447656', 'pwd': '123456'}
        self.login_resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=self.login_data)
        logger.info(self.login_resp.text)
    def tearDown(self):
        pass
    @data(*cases)
    def test_recharge(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        resp = requests.post(case.url,data=json.loads(case.data),cookies= self.login_resp.cookies)
        logger.info(resp.text)
        try:
            # 将返回结果和期望结果进行匹配
            self.assertEqual(case.expected,resp.json()['code'],'recharge error')
            # 一致就写入Excel的结果为Pass
            self.do_excel.write_result('recharge',case.id+1, resp.text, 'Pass')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            # 不一致就写入Excel的结果为Fail，并抛出异常
            self.do_excel.write_result('recharge',case.id+1,resp.text,'Fail')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

