#coding=gbk
import os
import string
os.chdir('D:/')#���ò���·��
print os.getcwd()
f=open('��������ҹ.txt')
try:
    for each_line in f:
        try:
            (upper,lower)=each_line.split('��',1)#���ѵ�ͬʱĨ����
            print '�Ͼ䣺'+upper+'  �¾䣺'+lower.rstrip('��\n')#ȥ��lower�ַ������ұߵġ��ͻ��з�
        except ValueError:
            print each_line.rstrip()
except IOError as err:
    print('File Error:'+str(err))
finally:
    if 'f' in locals():
        f.close()
input()