#coding=gbk
import random
def mid(n,k):
    i,j,s,e=1,9,0,9#i,j������ָ�룬s,e��¼��һ�δ���Ŀ�ʼ�ͽ���λ��
    while True:
        i=s+1
        j=e
        while i<j:
            while n[i]<n[s] and i!=e:#���ָ���ƶ���i!=e��ֹԽ��
                i+=1
            while n[j]>=n[s] and j!=s:#�ұ�ָ���ƶ���j!=s��ֹԽ��
                j-=1
            if i<j:
                n[i],n[j]=n[j],n[i]#�������jָ��λ�õ�Ԫ�ؽ��л���
        if n[s]>n[j]:
            n[s],n[j]=n[j],n[s]#�����������б�����СԪ�ص����
        if j>k:#�ı���һ�ε�������ʼ����ֹλ��
            e=j-1
        elif j<k:
            s=j+1
        else:
            print '�б��',k+1,'С��Ԫ���ǣ�',n[j]
            break
if __name__=="__main__":
    n=[]
    i=0
    while i<10:
        t=random.randint(1,100)#��������б�
        n.append(t)
        i+=1
    print n
    mid(n,5)
    input()