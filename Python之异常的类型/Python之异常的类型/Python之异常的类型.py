#coding=gbk
import os
try:
    print a
except NameError as err:
    print 'NameError:���Է���û�������ı���'
    print err
a='��������ҹ��'
try:
    a.rstp('��')
except AttributeError as err:
    print 'AttributeError:���ò����ڵķ��������Է���δ֪�Ķ�������'
    print err
def rstp(a,i):
    print a.rstrip(i)
#rstp(a,'��\n')
d={"a":1, "b":"abc"}
try:
    d["c"]
except KeyError as err:
    print 'KeyError:����һ�������ڵ��ֵ�ؼ���'
    print err
d=[233,344]
try:
    d[3]
except IndexError as err:
    print 'IndexError:���������б�Χ'
    print err
try:
    5/0
except ZeroDivisionError as err:
    print 'ZeroDivisionError:����Ϊ0'
    print err
a=1
try:
    a+='ss'
except TypeError as err:
    print 'TypeError:δ����ǿ��ת���ͷǷ���������'
    print err
try:
    f=open('һ�������ڵ��ļ�.txt')
except IOError as err:
    print 'IOError:�����������'
    print err
a
try:
    a+=1
except UnboundLocalError as err:
    print 'UnboundLocalError:�ֲ�����û��ֵ��ʹ��'
    print err
input()
