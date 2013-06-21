#coding=gbk
import random
def extend(a,b,n):
    c=0
    for i in a:
        i.append(b[c])
        c+=1
def gauss(a):
    c=0
    while c!=len(a):
        for i in range(c+1,len(a)):
            temp=float(a[i][c])/float(a[c][c])
            for j in range(c,len(a)+1):
                '''
                print 'c-',c
                print 'i-',i
                print 'j-',j
                print 'temp',temp
                print 'aij',a[i][j]
                print '/',float(a[i][c])/float(a[c][c])
                print 'aij',a[i][j]
                '''
                a[i][j]=a[i][j]-a[c][j]*temp#这里不能用-=.........    
        c+=1
    print 'na-',a
if __name__=="__main__":
    n=3
    a=[[random.randint(1,20) for i in range(n)] for i in range(n)]#随机二维数组的生成
    b=[random.randint(1,100) for i in range(n)]
    print 'a-',a
    print 'b-',b
    extend(a,b,n)
    gauss(a)
    input()