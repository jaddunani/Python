#2. Create a Python package that contains two or more modules. Each module should
#define classes with attributes and methods. Then create another module outside
#the package, import the package modules, and create a subclass that inherits
#from at least one of the classes. Finally, create objects of both parent and
#child classes.

class A:
    def __init__(self,a):
        self.a=a
    def m1(self,b):
        self.a+=b
        print(self.a)