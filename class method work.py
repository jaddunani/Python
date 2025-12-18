''''
class A:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def _passed(self):
        if self.marks>40:
            return True
        else:
            return False
obj=A("A",100)
obj1=A("B",39)
print(obj._passed())
print(obj1._passed())
'''
from operator import truediv

''''
class Employee:
    name=" "
    company_name="TechCorp"
    @classmethod
    def change_company(cls,New_name):
        cls.company_name=New_name
        return cls.company_name

obj=Employee()
obj.change_company("cv corp")
print(obj.company_name)
'''

'''
class MathOps():
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
obj=MathOps()
print(obj.is_even(3))
print(MathOps.is_even(4))
'''

'''
class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print(self.mileage)
        print(self.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.new_wheels=new_wheels
        return cls.new_wheels
obj=Car(20)
obj.display_specs()
print(obj.change_wheels(6))
'''


#Q5. Create a class Temperature with:
#•	instance attribute celsius
#•	a static method to_fahrenheit(celsius)
#•	an instance method show_conversion() that uses the static method to print both values.
'''
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        # Formula: (°C × 9/5) + 32 = °F
        return (celsius * 9/5) + 32

    def show_conversion(self):
        fahrenheit = Temperature.to_fahrenheit(self.celsius)
        print(f"{self.celsius}°C = {fahrenheit}°F")
o1=Temperature(32)
o1.show_conversion()
'''






#Create a class Book with:
#•	instance attributes title, author
#•	a class variable total_books
#•	a class method from_string(cls, book_str) that creates an object from "title-author" format
#•	a static method is_valid_title(title) that checks if title has at least 3 characters
#•	increment total_books for every book created

class Book:
    total_books=0
    def __init__(self,t,a):
        self.t=t
        self.a=a
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        cls.total_books+=1
        return cls(t,a)
    @staticmethod
    def is_valid(s):
        s=len(s)
        if s>=3:
            return True
        else:
            return False

Book.from_string("su-sa")
print(Book.total_books)
B1=Book("sujhhugytftr","sa")
print(B1.t)
print(Book.is_valid(B1.t))







