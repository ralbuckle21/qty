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
for i in ln:
    f.write(i)
    if count%2==0:
        f.write('��')
    else:
        f.write('��\n')
    count+=1
input()
