#coding=gbk
def jt(n):
    print '���ɴ�1��',n,'�ļ���������'
    dir=[-1 for i in range(n+2)]#������ʼ���ķ�����False������True������
    res=range(n+1)
    res.append(10000)#res�б�������Ľ���б������ĵ�һ��Ԫ�غ����һ��Ԫ����Ϊ�ǳ����ֵ����Ϊ��ֹ�㷨Խ���'ǽ'
    res[0]=10000
    print res[1:n+1]
    count=1
    while True:
        i=1#i�������ڽ��бȽϵ�Ԫ���±꣬��1��ʼ��n����
        j=0
        while i!=n+1:
            if res[i]>res[i+dir[i]] and (j==0 or res[i]>res[j]):
                j=i;#j�Ǽ��������ƶ���Ԫ���±�
            i+=1
        if j==0:#���û�п����ƶ���Ԫ�أ�
            break
        temp=dir[j]#��ʱ��סjԪ�ص��ƶ�����
        res[j],res[j+dir[j]]=res[j+dir[j]],res[j]#pythonʽswap
        if dir[j]==-1:
            t=dir[j]
            dir[j]=dir[j-1]
            dir[j-1]=t
        else:
            t=dir[j]
            dir[j]=dir[j+1]
            dir[j+1]=t
        j+=temp
        print res[1:n+1]#���һ�����н��
        count+=1
        i=1
        while i!=n+1:#��ת���ƶ�Ԫ�ش��Ԫ�صķ���
            if res[i]>res[j]:
                dir[i]=-dir[i]
            i+=1
    print '�ܼƣ�',count,'��Ԫ��'
        
if __name__=="__main__":
    jt(6)
    input()