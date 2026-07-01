# class animal():
#     def speak(self):
#         pass
# class dog(animal):
#     def speak(self):
#         print("wangwang")
#         return
# class cat(animal):
#     def speak(self):
#         print("miaomiao")
#         return
# class car():
#     def speak(self):
#         print("dididi")
#         return
# def make_noise(an:animal):
#     an.speak()
# if __name__ == "__main__":
#     a:animal=dog()
#     b:animal=cat()
#     c=car()
#     make_noise(a)
#     make_noise(b)
#     make_noise(c)
# class school():
#     teacher="wang"
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"你好{self.name}"
#     @classmethod
#     def teach(cls,name):
#         t=cls(name)
#         print(t.name)
#         print(t)
#         return
#     @staticmethod
#     def tt():
#         print(school.teach("liu"))
# if  __name__=="__main__":
#     stu=school("zhang")
#     print(stu)
#     stu.tt()
#     stu.teach("zhao")
#     school.teach("niu")
#
""""

闭包

"""
# def decorate(func):
#     def inner():
#         print("你好啊")
#         func()
#     return inner
#
# @decorate
# def name():
#     print("石哥哥")
# name()
# print('-'*24)
# def decorate(func):
#     def inner(a):
#         print("你好啊")
#         func(a)
#     return inner
# @decorate
# def name(x):
#     print(x)
# name("石哥哥")
# print('-'*24)
# @decorate
# def name():
#     print("石哥哥")
# name()
# print('-'*24)
# def decorate(func):
#     def inner():
#         print("你好啊")
#         return func()
#     return inner
# @decorate
# def add():
#     a=10
#     b=20
#     return a+b
# x=add()
# print(x)
# print('-'*24)
# def decorate(func):
#      def inner(x,y):
#          print("你好啊")
#          return func(x,y)
#      return inner
# @decorate
# def add(a,b):
#      return a+b
# x=add(33,33)
# print(x)
# def decorate(func):
#     def inner(*args, **kwargs):
#         print("正在计算中...")
#         return func(*args, **kwargs)
#     return inner
# @decorate
# def get_sum(*args, **kwargs):
#     return sum(args)+sum(kwargs.values())
# s=get_sum(1,2,3,a=1,b=2,c=3)
# print(s)
# def out(flag):
#     def decorator(func):
#         def inner(x,y):
#             if flag=='+':
#                 print("加法计算中！！！")
#                 return func(x,y)
#             elif flag=='-':
#                 print("减法计算中！！！")
#                 return func(x,y)
#         return inner
#     return decorator
# @out('+')
# def add(x,y):
#     return x+y
# @out('-')
# def sub(x,y):
#     return x-y
# a=add(9,1)
# print(a)
# b=sub(9,1)
# print(b)
"""
深浅拷贝
    浅拷贝：可变拷贝一层
    深拷贝：可变拷贝深层
    不可变两者相当于指针赋值
"""
import copy
def demo1():
    a=[1,2,3]
    b=[4,5,6]
    c=[6,7,a,b]
    a[1]=66
    b[1]=88
    d=copy.copy(c)
    print(c)
    print(d)
    print(id(c))
    print(id(d))
def demo2():
    a=(1,2,3)
    b=(4,5,6)
    c=(6,7,a,b)
    d=copy.copy(c)
    print(c)
    print(d)
    print(id(c))
    print(id(d))
def demo3():
    a=[1,2,3]
    b=[4,5,6]
    c=[6,7,a,b]
    d=copy.deepcopy(c)
    a[1]=66
    b[1]=88
    print(c)
    print(d)
    print(id(c))
    print(id(d))
def demo4():
    a = (1, 2, 3)
    b = (4, 5, 6)
    c = (6, 7, a, b)
    d = copy.deepcopy(c)
    print(c)
    print(d)
    print(id(c))
    print(id(d))
if __name__ == '__main__':
    demo1()
    demo2()
    demo3()
    demo4()