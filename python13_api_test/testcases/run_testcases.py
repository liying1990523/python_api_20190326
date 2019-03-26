# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/27 17:11
@Author  : 
@function： 运行测试用例
"""
import unittest
from common import constants
from libext import HTMLTestRunnerNew

discover = unittest.defaultTestLoader.discover(constants.testcases_dir,'test_*.py',top_level_dir=None)
with open(constants.report_html,'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='接口测试',
                                              description='API测试报告',
                                              tester='Mongo'
                                              )
    runner.run(discover)