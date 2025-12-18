class A():
    a=[]
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def m1(self):
        a.append(self.x)
        a.append(self.y)
a=[]
obj=A(2,3)
obj.m1()
print(a)