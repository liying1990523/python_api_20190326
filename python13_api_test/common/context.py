# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/25 14:36
@Author  : 
@function：替换字符串
"""
import re
# s是目标字符串
# dict是替换的内容，字典
# 找到目标字符串里面的标识符KEY，去dict里面拿到替换的值
# 替换到s 里面去，然后再返回
from common.config import ReadConfig
config = ReadConfig()
class Context: # 上下文，数据的准备和记录
    admin_user = config.get('data', 'admin_user')
    admin_pwd = config.get('data','admin_pwd')
    loan_member_id = config.get('data','loan_member_id')
    normal_user = config.get('data','normal_user')
    normal_pwd = config.get('data','normal_pwd')
    normal_member_id = config.get('data','normal_member_id')

def replace1(s,dict):
    p = '\$\{(.*?)}' #正则表达式
    while re.search(p,s):
        m = re.search(p,s)
        g = m.group(1)
        value = dict[g]
        s = re.sub(p,value,s,count=1) #查找并替换找到的第一个
    return s
def replace(s):
    p = '\$\{(.*?)}' #正则表达式
    while re.search(p,s):
        m = re.search(p,s)
        key = m.group(1)
        if hasattr(Context,key):
            value = getattr(Context,key)
            s = re.sub(p,value,s,count=1) #查找并替换找到的第一个,sub函数中value不能为None
        else:
            return None
            # return 'Context中不存在属性{0}'.format(key) #返回None或者抛出一个异常，告知没有这个属性
    return s

if __name__ == '__main__':
    s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
    # data = {'admin_user': None, 'admin_pwd': None}
    # s = replace1(s,data)
    s = replace(s)
    print(s)