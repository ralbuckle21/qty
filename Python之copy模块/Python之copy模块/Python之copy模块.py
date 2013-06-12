#coding=gbk
import copy
a=[[1],[2],[3]]
print '用copy进行处理，对象是容器时成员仍然指向原来的成员对象'
b=copy.copy(a)
print 'a=',a
print 'b=',b
a[0][0]=0
a[1][0]=None
print 'a=',a
print 'b=',b
print '用deepcopy进行处理'
a=[[1],[2],[3]]
b=copy.deepcopy(a)
print 'a=',a
print 'b=',b
a[0][0]=0
a[1][0]=None
print 'a=',a
print 'b=',b
input()