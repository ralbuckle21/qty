#coding=gbk
import random
def mid(n,k):
    i,j,s,e=1,9,0,9#i,j是左右指针，s,e记录了一次处理的开始和结束位置
    while True:
        i=s+1
        j=e
        while i<j:
            while n[i]<n[s] and i!=e:#左边指针移动，i!=e防止越界
                i+=1
            while n[j]>=n[s] and j!=s:#右边指针移动，j!=s防止越界
                j-=1
            if i<j:
                n[i],n[j]=n[j],n[i]#将中轴和j指针位置的元素进行互换
        if n[s]>n[j]:
            n[s],n[j]=n[j],n[s]#处理中轴是列表中最小元素的情况
        if j>k:#改变下一次迭代的起始和终止位置
            e=j-1
        elif j<k:
            s=j+1
        else:
            print '列表第',k+1,'小的元素是：',n[j]
            break
if __name__=="__main__":
    n=[]
    i=0
    while i<10:
        t=random.randint(1,100)#生成随机列表
        n.append(t)
        i+=1
    print n
    mid(n,5)
    input()