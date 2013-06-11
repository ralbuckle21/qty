#coding=gbk
# -*- coding: UTF-8 -*-
import os
import time

print('是否存在名为"春江花月夜.txt"的文件：'+repr(os.path.exists('春江花月夜.txt')))#repr转化为字符串
print('是否存在名为"春江花月夜.exe"的文件：'+repr(os.path.exists('春江花月夜.exe')))
print('是否存在名为"长恨歌.txt"的文件：'+repr(os.path.exists('长恨歌.txt')))
print('春江花月夜.txt的文件大小：'+repr(os.path.getsize('春江花月夜.txt')))
print('春江花月夜.txt的绝对路径：'+os.path.abspath('春江花月夜.txt'))
print('D盘根目录下的文件"春江花月夜.txt"的路径标准化：'+os.path.normpath('D:\\春江花月夜.txt)'))
print('春江花月夜.txt的最新访问时间：'+repr(time.localtime(os.path.getatime('春江花月夜.txt'))))
print('春江花月夜.txt的最新修改时间：'+repr(time.localtime(os.path.getmtime('春江花月夜.txt'))))
print('春江花月夜.txt的最新状态改变时间：'+repr(time.localtime(os.path.getctime('春江花月夜.txt'))))

input()