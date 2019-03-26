# -*- coding:utf-8 -*-
""" 
@Time    : 2019/2/25 16:19
@Author  : 
@function：反射
静态--运行前，如果要调用类的属性或者方法，就需要实例化它的对象
动态--运行时，就可以获取类的属性或者方法，甚至更改它的属性或者方法
"""
class Girls:
    sex = 'nv'
    name = 'name'
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.school = 'pupil'

    def sings(self):
        print(self.name+'会唱歌')

if __name__ == '__main__':
    g = Girls('lili',18)
    print(g.__dict__.items())
    # print(g.name)
    # g.sings()
    #
    # setattr(g,'hobby','swimming') #给类或者实例对象动态的添加属性或者方法，
    #                       # 若给实例对象添加，则作用域为当前实例对象
    # print(g.hobby)
    #
    # setattr(Girls,'work','teacher') #给类动态的添加属性，添加的属性变成类属性
    # g2 = Girls('mongo',19)
    # # print(g2.hobby) #AttributeError: 'Girls' object has no attribute 'hobby'
    # print(g2.work) #teacher
    # print(getattr(Girls,'work')) #用类调用类属性
    # print(getattr(g2, 'work')) #用对象调用类属性
    # g3 = Girls('mongo',19)
    # print('g3.work:',g3.work) #用对象调用类属性
    # print('Girls.work:', Girls.work) #用类调用类属性
    # print(getattr(Girls, 'sex'))
    # print(getattr(g3, 'sex'))
    # # print(getattr(Girls, 'school')) #初始化函数里的属性是对象属性，对象属性只能对象调用，所以此处报错
    # print(getattr(g3, "sings"))  # 获取sings方法，存在就打印出方法的内存地址
    #                             # <bound method Girls.sings of <__main__.Girls object at 0x0000000002212D68>>
    # getattr(g3, "sings")()  # 获取sings方法，后面加括号可以将这个方法运行
    # print(hasattr(Girls,'name')) #根据属性名获取类的属性，当属性不存在时返回False
    # print(hasattr(Girls,'age')) #判断当前这个类有没有这个实例属性，有就返回True，没有返回False
    # print(hasattr(g3,'age'))#判断这个对象是否有这个实例属性
    #
    # delattr(g2,'age') #删除对象属性，仅在当前对象有效
    # print(hasattr(g2,'age')) #False
    # print(hasattr(g3, 'age')) #True
    # delattr(Girls,'sex') #删除类属性
    # print(hasattr(Girls,'sex')) #False
    # print(hasattr(g3,'sex')) #False