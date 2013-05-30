#coding=gbk
import codecs
import sys
print('请输入第一个文件:')
while True:
    Fname=raw_input()
    input=open(Fname,'r')
    Slist1=input.readlines()
    if '#TYPE_WORD' in Slist1[0] and Slist1[1][0]=='#' and Slist1[2][0]=='#' and Slist1[2][5]==Slist1[2][8]=='-':
        print('输入文件:'+Fname)
        input.close()
        break;
    else:
        print('输入的不是有效的词库文件,请重新输入')
        continue;
print('请输入第二个文件:')
while True:
    Fname=raw_input()
    input=open(Fname,'r')
    Slist2=input.readlines()
    if '#TYPE_WORD' in Slist2[0] and Slist2[1][0]=='#' and Slist2[2][0]=='#' and Slist2[2][5]==Slist2[2][8]=='-':
        print('输入文件:'+Fname)
        input.close()
        break
    else:
        print('输入的不是有效的词库文件')
        input.close()
        continue
if(Slist1[1]!=Slist2[1]):
    print('两个文件不属于同一个用户')
    sys.exit()
Slength=len(Slist1)-3
myList=[[] for i in range(Slength)]
if Slist1[2][1:5]>Slist2[2][1:5]:
    select='later'
elif Slist1[2][1:5]<Slist2[2][1:5]:
    select='earlier'
else:
    if Slist1[2][6:8]>Slist2[2][6:8]:
        select='later'
    elif Slist1[2][6:8]<Slist2[2][6:8]:
        select='earlier'
    else:
        if Slist1[2][9:11]>Slist2[2][9:11]:
            select='later'
        elif Slist1[2][9:11]<Slist2[2][9:11]:
            select='earlier'
        else:
            select='same'
x=0
if select=='earlier':
    while x!=Slength:
        myList[x].append(Slist1[x+3])
        myList[x].append(Slist2[x+3])
        x+=1
else:
    while x!=Slength:
        myList[x].append(Slist1[x+3])
        myList[x].append(Slist2[x+3])
        x+=1
for y in myList:
    print(y)
raw_input()