#coding=gbk
import os
import string
os.chdir('D:/')#设置操作路径
print os.getcwd()
f=open('春江花月夜.txt')
try:
    for each_line in f:
        try:
            (upper,lower)=each_line.split('，',1)#分裂的同时抹掉，
            print '上句：'+upper+'  下句：'+lower.rstrip('。\n')#去除lower字符串最右边的。和换行符
        except ValueError:
            print each_line.rstrip()
except IOError as err:
    print('File Error:'+str(err))
finally:
    if 'f' in locals():
        f.close()
input()