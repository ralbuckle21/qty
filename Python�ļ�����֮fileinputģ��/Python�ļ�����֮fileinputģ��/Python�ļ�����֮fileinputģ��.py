#coding=gbk
import fileinput
import glob
import sys
for line in fileinput.input("1/��������ҹ.txt"):
    print sys.stdout.write(line)
print fileinput.filename()#�ļ���

input()