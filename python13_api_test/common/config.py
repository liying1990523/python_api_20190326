# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/21 14:33
@Author  : 
@function： 读取配置文件
"""
import configparser
from common import constants

# # 1、实例化对象
# config = configparser.ConfigParser()
# # 2、加载文件
# config.read(constants.test_conf)
# # 3、获取信息
# rest = config.get('api', 'pre_url')  # 利用get方法获取的信息都是字符串类型
# print(type(rest), rest)
# port = config.get('db', 'port')
# print(type(port), port)
# port_int = config.getint('db', 'port')
# print(type(port_int), port_int)

class ReadConfig:
    def __init__(self):
        # 实例化对象
        self.config = configparser.ConfigParser()
        # 加载global.conf文件，用来选择测试环境
        self.config.read(constants.global_conf, encoding='utf-8')
        open = self.config.getboolean('swith', 'open')
        if open:
            self.config.read(constants.test_conf, encoding='utf-8')  # 选择test.conf中环境配置
        else:
            self.config.read(constants.test2_conf, encoding='utf-8')  # 选择test2.conf中环境配置

    def get(self, section, option):
        try:
            return self.config.get(section, option)
        except configparser.NoSectionError:
            return '不存在此section:{0}'.format(section)
        except configparser.NoOptionError:
            return '不存在此option:{0}'.format(option)

    def getboolean(self, section, option):
        try:
            return self.config.getboolean(section, option)
        except configparser.NoSectionError:
            return '不存在此section:{0}'.format(section)
        except configparser.NoOptionError:
            return '不存在此option:{0}'.format(option)

    def getint(self, section, option):
        try:
            return self.config.getint(section, option)
        except configparser.NoSectionError:
            return '不存在此section:{0}'.format(section)
        except configparser.NoOptionError:
            return '不存在此option:{0}'.format(option)

if __name__ == '__main__':
    config = ReadConfig()
    print(config.get('api','pre_url'))