# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/27 9:06
@Author  :
@function： 日志输出
"""
import logging
import logging.handlers

# 1、定义收集器，并给收集器指定级别
my_logger = logging.getLogger('testlogger')
my_logger.setLevel('DEBUG')
# 设置日志输出格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]")
# 2、指定输出渠道，并给渠道设置级别
ch = logging.StreamHandler() # 输出到控制台
ch.setLevel('DEBUG')
ch.setFormatter(formatter)
# fh = logging.FileHandler('test.log',encoding='utf-8') # 输出到文件
fh = logging.handlers.RotatingFileHandler('test.log',maxBytes=20*1024*1024, backupCount=10,encoding='utf-8')
fh.setLevel('DEBUG')
fh.setFormatter(formatter) # 设置输出格式
# 3、对接 日志收集器与输出渠道 进行对接
my_logger.addHandler(fh)
my_logger.addHandler(ch)

my_logger.debug('123')
my_logger.warning('456')
# 去掉重复日志 每次收集完毕之后，移除Handler
my_logger.removeHandler(ch)
my_logger.removeHandler(fh)