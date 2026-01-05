from exam.q1a import *
from functools import reduce
class con(base):
    def calc(self,l):
        l1=list(filter(lambda x:x%5==0,map(lambda x:x*2,l)))
        print(l1)
        l2=reduce(lambda x,y:x+y,l1)
        print(l2)
