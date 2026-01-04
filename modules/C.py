from modules import *
from modules.A import Animal
from modules.B import Walkable


class dog(Animal,Walkable):
    def m1(self):
        pass
d=dog()
print(d.m1())
print(dog.mro())