# -*- coding:utf-8 -*-
""" 
@Time    : 2019/3/4 10:28
@Author  : 
@function： 
"""
from unittest import mock
from unittest.mock import Mock

import requests


def request_baidu():
    # 抓百度的内容
    return requests.get('https://www.baidu.com').text.encode('utf-8')


def print_baidu():
    print(request_baidu())


request_baidu = mock.Mock(return_value='this is baidu.')
print_baidu()

