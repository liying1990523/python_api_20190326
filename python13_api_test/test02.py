# -*- coding:utf-8 -*-
""" 
@Time    : 2019/3/26 10:42
@Author  : 
@function： 
"""
import time
words = "Dear, I love you forever!"
for char in words.split():
    allchar = []
    for y in range(12,-12,-1):
        lst = []
        lst_con = " "
        for x in range(-30,30):
            formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if formula<=0:
                lst_con += char[(x)%len(char)]
            else:
                lst_con += " "
        lst.append(lst_con)
        allchar += lst
    print('\n'.join(allchar))
    time.sleep(1)