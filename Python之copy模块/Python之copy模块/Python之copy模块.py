#coding=gbk
import copy
a=[[1],[2],[3]]
print '��copy���д�������������ʱ��Ա��Ȼָ��ԭ���ĳ�Ա����'
b=copy.copy(a)
print 'a=',a
print 'b=',b
a[0][0]=0
a[1][0]=None
print 'a=',a
print 'b=',b
print '��deepcopy���д���'
a=[[1],[2],[3]]
b=copy.deepcopy(a)
print 'a=',a
print 'b=',b
a[0][0]=0
a[1][0]=None
print 'a=',a
print 'b=',b
input()