#6. Create a class in a module that uses private attributes and @property /
#@setter decorators. Import the class into another module and show how
#encapsulation protects the data while still allowing controlled access.

class balance:
    def __init__(self,bal):
        self.__bal=bal
    @property
    def m1(self):
        return self.__bal
    @m1.setter
    def m2(self,new):
        self.__bal=new
