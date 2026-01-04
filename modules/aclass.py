#4. Create a package with a module containing an abstract base class (ABC).
#Another module in the same package should define concrete subclasses that
#implement all abstract methods. Write a driver program that imports these
#classes and demonstrates polymorphism.



from abc import ABC,abstractmethod
class shop(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass