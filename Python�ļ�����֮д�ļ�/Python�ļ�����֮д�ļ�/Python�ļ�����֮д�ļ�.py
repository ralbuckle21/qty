#coding=gbk
import os
import sys
import shutil
f=open('��������ҹ.txt','w')#�Զ��ڴ�ʱ�������ļ�
f.write(' '*10+'��������ҹ'+'\n')
ln=['������ˮ����ƽ��','�������¹�������\n','�����沨ǧ���','�δ�������������\n']
f.writelines(ln)#ֱ������б�
ln=['������ת�Ʒ���','���ջ��ֽ�����','������˪������','͡�ϰ�ɳ������']
count=0
for i in ln:#����forѭ����д�뷽ʽ
    f.write(i)
    if count%2==0:
        f.write('��')
    else:
        f.write('��\n')
    count+=1#����input()���޷�����д����!
fi=open('��.txt','r')
lines=fi.readlines()
count=3#�������ิ��һ��
while count<len(lines):
    f.write(lines[count])
    count+=1
fi.close()
f.close()
f=open('��������ҹ.txt','r+')
lines=f.readlines()
count=7
f.write('\n')#���ƽ��Ϻ��˳�����...������������ˮ�����
while count<=9:
    f.write(lines[count])
    count+=1
f.close()
#��'������'���뵽'��������ҹ'֮��
f=open('��������ҹ.txt','r')
s=f.read()
f.close()
pos=s.find('��������ҹ')#pos��¼�ļ���'��������ҹ'�ַ�����λ��
pos+=len('��������ҹ')#Ϊ���ڴ�������ҹ֮�����
print pos
if pos!=-1:
    s=s[:pos]+'\n'+' '*(s.find('��������ҹ')+3)+'������'+s[pos:]
    f=open('��������ҹ.txt','w')
    f.write(s)
    f.close()
f=open('��������ҹ.txt','r')#�����ж�����ж�ɾ��
s=list(f.readlines())
del s[6],s[20:23]
f.close()
f=open('��������ҹ.txt','w')
for x in s:
    f.write(x)
f.close()
