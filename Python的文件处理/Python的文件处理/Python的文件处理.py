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
        os.remove('ddf.txt')#����ļ����ڣ���ɾ��Ŀ¼�µ��ļ�


    f=open('van.txt','r')
    print('van.txt�Ĵ�СΪ��')
    print(os.path.getsize('van.txt'))
    print('van.txt���ļ�����Ϊ��')
    print(os.stat('van.txt'))
    print('��readlines�������������,ͬʱȥ�����з�')
    for line in f.readlines():
        print(line.strip('\n'))
    f.close()

    
    #f=open('van.txt','w')
    #print('���ص�ǰ���λ�ã�')
    #print(f.tell())
    #f.seek(11)
    #f.write('TDN')
    

    print('�����ж�д�ķ�������һ���ļ�')
    fr=open('van.txt','r')
    fw=open('ddf.txt','w')#open��Ŀ���ļ�������ʱֱ�Ӵ���һ��
    fw.writelines(fr.read())
    fr.close()
    fw.close()


    print('��van.txt��darkholme.txt�����ָ��Ƶ���ǰĿ¼')
    shutil.copyfile("van.txt", "darkholme.txt")
    shutil.move("darkholme.txt", "darkholme.txt")
    '''
    ft=tempfile.mktemp('.txt')
    open(ft,'w').close()
    ftn=ft+'.copy'
    print(ft,ftn)
    '''
    input()