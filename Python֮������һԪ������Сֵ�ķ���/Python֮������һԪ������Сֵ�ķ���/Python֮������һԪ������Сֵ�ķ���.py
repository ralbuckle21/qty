#coding=gbk
#进退法确定一元单峰函数的极小值区间
#-----------------------------
# 入口：
#     f : 模型函数
#     Xa : 初始点
#     h : 步长
# 返回:
#     极小值区间[a,b]
# ----------------------------
def jinTui(f,Xa,h):
    if h==0:
        if Xa!=0:
            h=Xa*0.01
        else:
            h=0.01
    h=abs(h)#初始化步长
    fa=f(Xa)
    fh=f(Xa+h)#计算fa,fh
    if fa<fh:
        fa,fh=fh,fa#如果fa<fh,反向
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
def search3Min(f,a,b):#三分法求单峰函数极小值
    while True:
        dx=(b-a)/3#将极小值区间三等分
        x1=a+dx
        x2=a+2*dx
        f1=f(x1)
        f2=f(x2)
        if f1<=f2:#比较中间两个点的函数值，f1<f2则将右边界移向x2,f1>f2则将左边界移到x1
            b=x2
        else:
            a=x1
        if abs(b-a)<=1E-5*(abs(a)+abs(b)):
            return (a+b)/2
def search618( f , a , b ):#618法相对于三分法的优势：每次只需要计算一个分点，另一个分点是上一次计算过的
    a1=a+(b-a)*0.382
    b1=a+(b-a)*0.618
    f1=f(a1)
    f2=f(b1)
    while True:
        if f1<=f2:
            b=b1#右分点变成右界，左分点变成右分点
            b1=a1
            f2=f1
            a1=a+(b-a)*0.382
            f1=f(a1)
        else:#左分点变成左界，右分点变成左分点
            a=a1
            a1=b1
            f1=f2
            b1=a+(b-a)*0.618
            f2=f(b1)
        if abs(b-a)<=1E-5*(abs(a)+abs(b)):#如果上下分界已经足够接近，则选择它们
            return (a+b)/2    
def f(x):
    return (x-3)**2+10
Xa,h=100.0,0.5
a,b=jinTui(f,Xa,h)
print "[a,b]=[",a,",",b,"]"
Xmin=search3Min(f,a,b)
Ymin=f(Xmin)
print "三分法极小点=",Xmin, ",",Ymin
Xmin=search618(f,a,b)
Ymin=f(Xmin)
print "极小点=",Xmin,",",Ymin
input()