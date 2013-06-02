#coding=gbk
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
o="c:\\windows\\system32\\shutdown -s "
from time import ctime, sleep
import sys
import shutil
import tempfile
if  __name__ =="__main__": #main
    class Test_Me:
        def __init__(self,color):
            self.__color = color
            pass
        def getColor(self):
            return self.__color
            pass
        def setColor(self,color):
            self.__color = color
            pass
    obj = Test_Me('green')
    print obj.getColor()
    obj.setColor('blue')
    print obj.getColor()

    if os.path.isfile('darkholme.txt'):
        os.remove('darkholme.txt')
    if os.path.isfile('ddf.txt'):
        os.remove('ddf.txt')#如果文件存在，则删除目录下的文件


    f=open('van.txt','r')
    print('van.txt的大小为：')
    print(os.path.getsize('van.txt'))
    print('van.txt的文件属性为：')
    print(os.stat('van.txt'))
    print('用readlines方法输出所有行,同时去除换行符')
    for line in f.readlines():
        print(line.strip('\n'))
    f.close()

    
    #f=open('van.txt','w')
    #print('返回当前光标位置：')
    #print(f.tell())
    #f.seek(11)
    #f.write('TDN')
    

    print('用逐行读写的方法复制一个文件')
    fr=open('van.txt','r')
    fw=open('ddf.txt','w')#open在目标文件不存在时直接创建一个
    fw.writelines(fr.read())
    fr.close()
    fw.close()


    print('将van.txt以darkholme.txt的名字复制到当前目录')
    shutil.copyfile("van.txt", "darkholme.txt")
    shutil.move("darkholme.txt", "darkholme.txt")
    '''
    ft=tempfile.mktemp('.txt')
    open(ft,'w').close()
    ftn=ft+'.copy'
    print(ft,ftn)
    '''
    input()