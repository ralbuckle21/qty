#coding=gbk
# -*- coding: UTF-8 -*-
import os
import time

print('�Ƿ������Ϊ"��������ҹ.txt"���ļ���'+repr(os.path.exists('��������ҹ.txt')))#reprת��Ϊ�ַ���
print('�Ƿ������Ϊ"��������ҹ.exe"���ļ���'+repr(os.path.exists('��������ҹ.exe')))
print('�Ƿ������Ϊ"���޸�.txt"���ļ���'+repr(os.path.exists('���޸�.txt')))
print('��������ҹ.txt���ļ���С��'+repr(os.path.getsize('��������ҹ.txt')))
print('��������ҹ.txt�ľ���·����'+os.path.abspath('��������ҹ.txt'))
print('D�̸�Ŀ¼�µ��ļ�"��������ҹ.txt"��·����׼����'+os.path.normpath('D:\\��������ҹ.txt)'))
print('��������ҹ.txt�����·���ʱ�䣺'+repr(time.localtime(os.path.getatime('��������ҹ.txt'))))
print('��������ҹ.txt�������޸�ʱ�䣺'+repr(time.localtime(os.path.getmtime('��������ҹ.txt'))))
print('��������ҹ.txt������״̬�ı�ʱ�䣺'+repr(time.localtime(os.path.getctime('��������ҹ.txt'))))
def dump(st):#����һ���ļ��ĸ�������ֵ
    mode,ino,dev,nlink,uid,gid,size,atime,mtime,ctime=st
    print "-�ļ���С:",size,"bytes"
    print "-ӵ����:",uid,gid
    print "-����ʱ��:",time.ctime(ctime)
    print "-����״̬�ı�ʱ��:",time.ctime(atime)
    print "-�����޸�ʱ��:",time.ctime(mtime)
    print "-ģʽ:",oct(mode)
    print "-inode/dev:",ino,dev
st=os.stat('��������ҹ.txt')
print '����-'+'��������ҹ.txt'
dump(st)
f=open('��������ҹ.txt','r')#����һ���򿪵��ļ��ĸ�������
st=os.fstat(f.fileno())
print '����-'+'��������ҹ.txt'
dump(st)

input()