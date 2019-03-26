# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/27 9:06
@Author  :
@function： 日志输出
"""
import logging
import logging.handlers
from common import constants
import os
from common.config import ReadConfig

config = ReadConfig()

def get_logger(logger_name):
    # 1、定义收集器，并给收集器指定级别
    my_logger = logging.getLogger(logger_name)
    my_logger.setLevel('DEBUG')
    # 设置日志输出格式
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]")
    # 2、指定输出渠道，并给渠道设置级别
    file_name = os.path.join(constants.logs_dir,'test.log')
    fh = logging.handlers.RotatingFileHandler(file_name,maxBytes=20*1024*1024, backupCount=10,encoding='utf-8')
    fh_level = config.get('log','file_handler_level')
    fh.setLevel(fh_level)
    fh.setFormatter(formatter) # 设置输出格式

    console_handler = logging.StreamHandler()
    level = config.get('log', 'console_handler')
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    # 3、对接 日志收集器与输出渠道 进行对接
    my_logger.addHandler(fh)
    my_logger.addHandler(console_handler)

    return my_logger


if __name__ == '__main__':
    logger = get_logger('login')
    logger.info('111')
