"""
@function：充值的测试用例 ，利用session
"""
import unittest

from common.request import Request
from common.do_excel import DoExcel
from common import constants
from libext.ddtnew  import ddt,data
from common import logger

logger = logger.get_logger('cases')
@ddt
class LoginTest(unittest.TestCase):
    do_excel = DoExcel(constants.case_file) # 读取cases.xlsx
    cases = do_excel.get_cases('recharge') # 指定读取recharge测试数据

    @classmethod
    def setUpClass(cls): # 每个测试类里面去运行的操作放到类方法里面
        logger.debug('这是一个类方法\n')
        cls.request = Request()  # 实例化对象
    @classmethod
    def tearDownClass(cls):
        cls.request.close() #关闭session
    def setUp(self): # 每个测试方法里面去运行的操作放到setUp里面
        logger.debug('这是一个对象方法')
        pass
    def tearDown(self):
        pass
    @data(*cases)
    def test_recharge(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method,case.url,case.data)
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

