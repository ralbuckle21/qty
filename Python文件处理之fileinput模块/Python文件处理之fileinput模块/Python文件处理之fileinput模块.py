#coding=gbk
import fileinput
import glob
import sys
for line in fileinput.input("1/春江花月夜.txt"):
    print sys.stdout.write(line)
print fileinput.filename()#文件名

input()