#coding=gbk
#���˷�ȷ��һԪ���庯���ļ�Сֵ����
#-----------------------------
# ��ڣ�
#     f : ģ�ͺ���
#     Xa : ��ʼ��
#     h : ����
# ����:
#     ��Сֵ����[a,b]
# ----------------------------
def jinTui(f,Xa,h):
    if h==0:
        if Xa!=0:
            h=Xa*0.01
        else:
            h=0.01
    h=abs(h)#��ʼ������
    fa=f(Xa)
    fh=f(Xa+h)#����fa,fh
    if fa<fh:
        fa,fh=fh,fa#���fa<fh,����
        Xa=Xa+h
        h=-h
    f1=fh
    while True:
        h=h+h
        f2=f(Xa+h)
        if f2>=f1:
            break
        else:
            f1=f2
    a,b=Xa,Xa+h
    if a>b:
        a,b=b,a
    return a,b
def search3Min(f,a,b):#���ַ��󵥷庯����Сֵ
    while True:
        dx=(b-a)/3#����Сֵ�������ȷ�
        x1=a+dx
        x2=a+2*dx
        f1=f(x1)
        f2=f(x2)
        if f1<=f2:#�Ƚ��м�������ĺ���ֵ��f1<f2���ұ߽�����x2,f1>f2����߽��Ƶ�x1
            b=x2
        else:
            a=x1
        if abs(b-a)<=1E-5*(abs(a)+abs(b)):
            return (a+b)/2
def search618( f , a , b ):#618����������ַ������ƣ�ÿ��ֻ��Ҫ����һ���ֵ㣬��һ���ֵ�����һ�μ������
    a1=a+(b-a)*0.382
    b1=a+(b-a)*0.618
    f1=f(a1)
    f2=f(b1)
    while True:
        if f1<=f2:
            b=b1#�ҷֵ����ҽ磬��ֵ����ҷֵ�
            b1=a1
            f2=f1
            a1=a+(b-a)*0.382
            f1=f(a1)
        else:#��ֵ�����磬�ҷֵ�����ֵ�
            a=a1
            a1=b1
            f1=f2
            b1=a+(b-a)*0.618
            f2=f(b1)
        if abs(b-a)<=1E-5*(abs(a)+abs(b)):#������·ֽ��Ѿ��㹻�ӽ�����ѡ������
            return (a+b)/2    
def f(x):
    return (x-3)**2+10
Xa,h=100.0,0.5
a,b=jinTui(f,Xa,h)
print "[a,b]=[",a,",",b,"]"
Xmin=search3Min(f,a,b)
Ymin=f(Xmin)
print "���ַ���С��=",Xmin, ",",Ymin
Xmin=search618(f,a,b)
Ymin=f(Xmin)
print "��С��=",Xmin,",",Ymin
input()