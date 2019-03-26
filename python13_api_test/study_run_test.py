# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/27 16:27
@Author  : 
@function： 运行测试用例
"""
import unittest
from testcases.test_login import LoginTest
suite = unittest.TestSuite() # 测试用例集合
loads = unittest.TestLoader() # 加载用例
suite.addTest(loads.loadTestsFromTestCase(LoginTest)) #批量加载 通过测试类来进行加载
runner = unittest.TextTestRunner()
runner.run(suite)
