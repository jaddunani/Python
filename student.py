class A:
    x=0
    def __init__(self):
        self.a=1
        self.b=2
        self.c=3
obj=A()
obj1=A()
print(obj.a,obj.b,obj.c)
print(obj1.a,obj1.b,obj1.c)
A.x=100
obj.x += 100
print(A.x)
print(obj.x,obj1.x)