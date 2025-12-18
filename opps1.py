#Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
#override it.
#Demonstrate polymorphism by iterating over a list of different animal objects and calling
#make_sound().


class Animal:
    def make_sound(self):
        print("it sounds like",end=" ")
class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("bow bow")
class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("meow meow")
class Cow(Animal):
    def make_sound(self):
        super().make_sound()
        print("ahamba")
animals=[Dog(),Cat(),Cow()]
for i in animals:
    i.make_sound()


#Q2. Write a function operate(device) that calls device.start().
#Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
#method, but share no inheritance relationship.
#Show that Python’s polymorphism works through behavior, not type


class Car:
    def start(self):
        print("engine started",end=" ")
class Computer:
    def start(self):
        print("system started",end=" ")
class washingMachine:
    def start(self):
        print("machine started",end=" ")

def operate(device):
    device.start()
    print("working")
c1=Car()
operate(c1)
c2=Computer()
operate(c2)
c3=washingMachine()
operate(c3)



#Q3. Create a Vector class that supports:
#• + operator → add coordinates
#• == operator → compare equality
#Show how operator overloading gives natural polymorphism to user-defined classes.


class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a+other.a,self.b+other.b
    def __eq__(self, other):
        return self.a==other.a and self.b==other.b

v1=Vector(2,3)
v2=Vector(2,3)
v3=v1+v2
v4=(v1==v2)
print(v3)
print(v4)


#Q4. Create a base class Transport with move() and derived classes Bus and Bike that
#override it but also call the parent implementation using super().
#Show the combination of reuse + custom behavior.


class Transport:
    def move(self):
        print("started",end=" ")
class Bus(Transport):
    def __init__(self,a):
        self.a=a
    def move(self):
        super().move()
        print(f"{self.a} moving")
class Bike(Transport):
    def __init__(self,b):
        self.b=b
    def move(self):
        super().move()
        print(f"{self.b} moving")
b1=Bus("bus")
b2=Bike("bike")
b1.move()
b2.move()



#Q6. Design:
#• Base class Payment with process(amount)
#• Subclass CreditCardPayment adds process(amount, card_type)
#Demonstrate what happens when overriding with different signatures and how Python
#handles it.

class Payment:
    def process(self,amount):
        print(f"balance in account is {amount}")
class Creditcardpayment(Payment):
    def process(self,amount,card_type=None):
        if card_type:
            print(f"balance in acount {amount} using {card_type} card" )
        else:
            super().process(amount)
p1=Creditcardpayment()
p1.process(500,"sbi")


#Q7. Create:
#• Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
#each implementing a different logic method.
#Demonstrate how polymorphism can be achieved without inheritance by using
#interchangeable strategy objects.



class Bs:
    def logic(self):
        print("x",end=" ")
class Ms:
    def logic(self):
        print("y",end=" ")
class Qs:
    def logic(self):
        print("z",end=" ")
class Sorter:
    def change(self,strategy):
        strategy.logic()
        print("running")
b = Bs()
m=Ms()
q=Qs()
s1 = Sorter()
s1.change(b)
s1.change(m)
s1.change(q)






#Q8. Create: • Base Account → withdraw() •
#Subclass SavingsAccount → modifies withdraw() •
#Subclass PremiumSavingsAccount → overrides again but calls parent using super()
#Show how polymorphism works across multiple levels


class Account:
    def __init__(self,b):
        self.b=b
    def withdraw(self, amount):
        print(f"balance={self.b},amount={amount},new_balance={self.b-amount}")


class SavingsAccount(Account):
    def __init__(self,a):
        super().__init__(a)
    def withdraw(self, amount):
        if self.b<amount:
            print("No sufficient balance in your account")
        else:
            print(f"balance={self.b},amount={amount},new_balance={self.b - amount}")
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self,a):
        super().__init__(a)
    def withdraw(self, amount):
        print("PremiumSavingsAccount: Premium rules activated")
        super().withdraw(amount)
p1=PremiumSavingsAccount(20000)
p1.withdraw(2100)




#Q9. Create a function draw(shape) that works for objects of
#classes Circle, Square, and Rectangle, each implementing a draw() method.
#Add another unrelated class Car with draw() and pass it — what happens and why?


class Circle:
    def draw(self):
        print("Drawing a Circle")
class Square:
    def draw(self):
        print("Drawing a Square")
class Rectangle:
    def draw(self):
        print("Drawing a Rectangle")
# Unrelated class
class Car:
    def draw(self):
        pass

def draw(shape):
    shape.draw()
c2=Square()
c1=Car()
draw(c1)
draw(c2)


#Q5. Using the abc module, create an abstract class Notification with send().
#Implement subclasses EmailNotification, SMSNotification, PushNotification — each
#with its own send() logic.
#Demonstrate polymorphism by looping over all and calling send().


from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class En(Notification):
    def send(self):
        print("EmailNotification")
class Sms(Notification):
    def send(self):
        print("SMSNotification")
class Pushn(Notification):
    def send(self):
        print("pushNotification")
e=En()
s=Sms()
p=Pushn()
e.send()
s.send()
p.send()
print(isinstance(e,En))
print(isinstance(s,En))
