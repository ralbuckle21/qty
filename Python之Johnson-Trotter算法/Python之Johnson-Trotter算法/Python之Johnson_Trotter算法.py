#coding=gbk
def jt(n):
    print '生成从1到',n,'的简单整数集合'
    dir=[-1 for i in range(n+2)]#批量初始化的方法，False代表左，True代表右
    res=range(n+1)
    res.append(10000)#res列表是输出的结果列表，将它的第一个元素和最后一个元素设为非常大的值，作为防止算法越界的'墙'
    res[0]=10000
    print res[1:n+1]
    count=1
    while True:
        i=1#i代表正在进行比较的元素下标，从1开始到n结束
        j=0
        while i!=n+1:
            if res[i]>res[i+dir[i]] and (j==0 or res[i]>res[j]):
                j=i;#j是即将进行移动的元素下标
            i+=1
        if j==0:#如果没有可以移动的元素，
            break
        temp=dir[j]#暂时记住j元素的移动方向
        res[j],res[j+dir[j]]=res[j+dir[j]],res[j]#python式swap
        if dir[j]==-1:
            t=dir[j]
            dir[j]=dir[j-1]
            dir[j-1]=t
        else:
            t=dir[j]
            dir[j]=dir[j+1]
            dir[j+1]=t
        j+=temp
        print res[1:n+1]#输出一次排列结果
        count+=1
        i=1
        while i!=n+1:#调转比移动元素大的元素的方向
            if res[i]>res[j]:
                dir[i]=-dir[i]
            i+=1
    print '总计：',count,'个元素'
        
if __name__=="__main__":
    jt(6)
    input()