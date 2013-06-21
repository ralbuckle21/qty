#coding=gbk
class Shift(object):
    def __init__(self, dec):
        self.__dec=dec
        self.__bin=self.__tobin()
    def __tobin(self):
        tmp=self.__dec
        result=''
        while tmp>0:
            mod=tmp%2
            result=str(mod)+result
            tmp/=2
        return result#result���ַ�����ʽ��
    def __todec(self, bin):
        result,i=0,0
        while i<len(bin):
            result+=int(bin[len(bin)-i-1])*(2**i)#��׼ת����ʸ
            i+=1
        return result
    def rightShift(self,times):#times���ƶ�λ��
        bin=self.__bin[-times:]+self.__bin[:-times]#bin����λ���ʮ��������__bin��ת��Ϊ��������ʽ��ԭʮ������
        return self.__todec(bin)#__todec����������ת��Ϊʮ������
    def leftShift(self,times):
        bin=self.__bin[times:]+self.__bin[:times]
        return self.__todec(bin)
def js(n,k):
    n=Shift(n)
    return n.leftShift(k-1)
if __name__ == "__main__":
    print js(8,2)
    input()