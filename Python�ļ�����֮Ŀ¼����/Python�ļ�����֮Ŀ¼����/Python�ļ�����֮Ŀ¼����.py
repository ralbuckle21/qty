#coding=gbk
import os
for files in os.listdir(os.getcwd()):
    print files
if os.path.exists('a')==False:
    os.makedirs('a/b/c') #a是b的根目录，b是c的根目录
if os.path.exists('一')==False:
    os.makedirs('一/二/三')
if os.path.exists('1')==False:
    os.makedirs('1/2/3')
os.removedirs('一/二/三')#注意不能只删除根目录
os.chdir('1')
print os.getcwd()
os.chdir(os.pardir)#返回当前目录的上一级，注意
print os.getcwd()
os.mkdir('fuck')
os.rmdir('fuck')#rmdir只能删除空目录
input()