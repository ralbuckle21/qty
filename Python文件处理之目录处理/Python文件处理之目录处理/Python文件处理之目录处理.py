#coding=gbk
import os
for files in os.listdir(os.getcwd()):
    print files
if os.path.exists('a')==False:
    os.makedirs('a/b/c') #a��b�ĸ�Ŀ¼��b��c�ĸ�Ŀ¼
if os.path.exists('һ')==False:
    os.makedirs('һ/��/��')
if os.path.exists('1')==False:
    os.makedirs('1/2/3')
os.removedirs('һ/��/��')#ע�ⲻ��ֻɾ����Ŀ¼
os.chdir('1')
print os.getcwd()
os.chdir(os.pardir)#���ص�ǰĿ¼����һ����ע��
print os.getcwd()
os.mkdir('fuck')
os.rmdir('fuck')#rmdirֻ��ɾ����Ŀ¼
input()