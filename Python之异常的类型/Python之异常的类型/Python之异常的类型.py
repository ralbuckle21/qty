#coding=gbk
import os
try:
    print a
except NameError as err:
    print 'NameError:尝试访问没有声明的变量'
    print err
a='春江花月夜。'
try:
    a.rstp('。')
except AttributeError as err:
    print 'AttributeError:引用不存在的方法，尝试访问未知的对象属性'
    print err
def rstp(a,i):
    print a.rstrip(i)
#rstp(a,'。\n')
d={"a":1, "b":"abc"}
try:
    d["c"]
except KeyError as err:
    print 'KeyError:请求一个不存在的字典关键字'
    print err
d=[233,344]
try:
    d[3]
except IndexError as err:
    print 'IndexError:索引超过列表范围'
    print err
try:
    5/0
except ZeroDivisionError as err:
    print 'ZeroDivisionError:除数为0'
    print err
a=1
try:
    a+='ss'
except TypeError as err:
    print 'TypeError:未经过强制转化就非法混用类型'
    print err
try:
    f=open('一个不存在的文件.txt')
except IOError as err:
    print 'IOError:输入输出错误'
    print err
a
try:
    a+=1
except UnboundLocalError as err:
    print 'UnboundLocalError:局部变量没赋值就使用'
    print err
input()
