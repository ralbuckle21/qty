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

input()