# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/22 10:50
@Author  : 
@function： 
"""
# import json
# s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
# dict = json.loads(s)
# print(type(dict))
# if dict['mobilephone'] == '${admin_user}':
#     dict['mobilephone'] = '18566743962'
# print(dict)
# # 字符串的查找、替换
# index = s.find('${admin_user}')
# print(index)
# if index > -1:
#     s = s.replace('${admin_user}','18566743962')
# print(dict)
# 正则方法
import re
# s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
data = {'admin_user':'18566743962','admin_pwd':'123456'}
# p = '\$\{admin_user}'
# m = re.search(p,s) #在给定字符串中寻找第一个匹配的子字符
# print(m)
p_re = '\$\{(.*?)}'
m1 = re.search(p_re,s)
g = m1.group(1) #组  正则表达式中()里表示的字符串 1表示第一个()的字符串
print(m1)
print(g)
s1 = re.sub(p_re,data[g],s,count=1) # 查找全部并替换，同时返回一个新字符串
print('sub练习，替换后：',s1)
l = re.findall(p_re,s) #查找全部，返回列表
print('findall查找全部，返回列表：',l)