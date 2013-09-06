#coding=gbk
import os
import sys
import shutil
f=open('春江花月夜.txt','w')#自动在打开时创建该文件
f.write(' '*10+'春江花月夜'+'\n')
ln=['春江潮水连海平，','海上明月共潮生。\n','滟滟随波千万里，','何处春江无月明。\n']
f.writelines(ln)#直接输出列表
ln=['江流宛转绕芳甸','月照花林皆似霰','空里流霜不觉飞','汀上白沙看不见']
count=0
for i in ln:
    f.write(i)
    if count%2==0:
        f.write('，')
    else:
        f.write('。\n')
    count+=1
input()
