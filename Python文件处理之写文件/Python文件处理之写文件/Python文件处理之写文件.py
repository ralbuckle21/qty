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
for i in ln:#利用for循环的写入方式
    f.write(i)
    if count%2==0:
        f.write('，')
    else:
        f.write('。\n')
    count+=1#加入input()则无法进行写操作!
fi=open('春.txt','r')
lines=fi.readlines()
count=3#这里故意多复制一行
while count<len(lines):
    f.write(lines[count])
    count+=1
fi.close()
f.close()
f=open('春江花月夜.txt','r+')
lines=f.readlines()
count=7
f.write('\n')#复制江畔何人初见月...但见长江送流水到最后
while count<=9:
    f.write(lines[count])
    count+=1
f.close()
#将'张若虚'插入到'春江花月夜'之后
f=open('春江花月夜.txt','r')
s=f.read()
f.close()
pos=s.find('春江花月夜')#pos记录文件中'春江花月夜'字符串的位置
pos+=len('春江花月夜')#为了在春江花月夜之后插入
print pos
if pos!=-1:
    s=s[:pos]+'\n'+' '*(s.find('春江花月夜')+3)+'张若虚'+s[pos:]
    f=open('春江花月夜.txt','w')
    f.write(s)
    f.close()
f=open('春江花月夜.txt','r')#把所有多余的行都删除
s=list(f.readlines())
del s[6],s[20:23]
f.close()
f=open('春江花月夜.txt','w')
for x in s:
    f.write(x)
f.close()
