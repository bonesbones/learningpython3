# _*_ coding:utf-8 _*_

L1 = ['HELLo','World',18,'Apple',None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]

print (L2)
