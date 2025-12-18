#  Create a base class Transport with move() and derived classes Bus
#  and Bike, which have the same "move" method but with different behaviour
#  it but also call the parent implementation using super().

class Transport:
    def __init__(self,license):
        self.l=license
    def move(self):
        print("moving",end=" ")
class bus(Transport):
    def __init__(self,a,name):
        super().__init__(a)
        self.name=name
    def move(self):
        super().move()
        print(f"{self.name} with license {self.l}")
class bike(Transport):
    def __init__(self, a, name):
        super().__init__(a)
        self.name = name
    def move(self):
        super().move()
        print(f"{self.name} with license {self.l}")
t1=bus(12,"bus")
t2=bike(16,"bike")
t1.move()
t2.move()





class Cvcorp:
    def __init__(self):
        self.apti=1
        self.commu=1
    def m1(self):
        print("teaches")
class Sql:
    def __init__(self,course):
        self.course=course
    def m1(self):
        print("sql")
    def t(self):
        print("yes")
class Python(Cvcorp,Sql):
    def __init__(self,a,b):
        Cvcorp.__init__(self)
        Sql.__init__(self,a)
        self.b=b
    def m1(self):
        super().m1()
        print(f"{self.course} and {self.b}")
p1=Python("sql","python")
print(p1.apti)
p1.m1()
p1.t()
print(Python.mro())



class work:
    def __init__(self,a):
        self.__a=a
    def getter(self):
        return self.__a
    def setter(self,new):
        self.__a=new
class sub(work):
    def __init__(self,b,c):
        super().__init__(b)
        self.c=c
    def add(self):
        return self.getter()+self.c
s=sub(3,4)
print(s.add())
