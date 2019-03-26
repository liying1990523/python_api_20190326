"""
@function：登录的测试用例
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
    cases = do_excel.get_cases('login') # 指定读取login测试数据
    request = Request() # 实例化对象
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @data(*cases)
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

