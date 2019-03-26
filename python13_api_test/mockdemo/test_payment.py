# -*- coding:utf-8 -*-
""" 
@Time    : 2019/3/4 11:10
@Author  : 
@function：
支付测试类：
1.正确的用户信息，支付成功
2，正确用户信息，支付失败
3，超时，超时再成功
4，超时，超时再失败
"""
import unittest
from mockdemo import payment
from unittest import mock

class RaymentTest(unittest.TestCase):
    def setUp(self):
        self.payment = payment.Payment()

    def test_success(self):
        self.payment.requestOutofSystem = mock.Mock(return_value=200)
        resp = self.payment.doPay(user_id=1,card_num='123456',amount=2000)
        self.assertEqual('success',resp)
    def test_fail(self):
        # side_effect 必须是元祖、列表。str,字典等iterate数据类型
        self.payment.requestOutofSystem = mock.Mock(return_value=500)
        resp = self.payment.doPay(user_id=1, card_num='123456', amount=2000)
        self.assertEqual('fail', resp)
    def test_retry_success(self):
        self.payment.requestOutofSystem = mock.Mock(side_effect=[TimeoutError,200])
        resp = self.payment.doPay(user_id=1, card_num='123456', amount=2000)
        self.assertEqual('success', resp)
    def test_retry_fail(self):
        self.payment.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
        resp = self.payment.doPay(user_id=1, card_num='123456', amount=2000)
        self.assertEqual('fail', resp)
