# Python Oops Question -1
# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().

class Animals:
    def make_sound(self):
        print("sounds like",end=" ")
class Dog(Animals):
    def make_sound(self):
        super().make_sound()
        print("bow bow")
class Cat(Animals):
    def make_sound(self):
        super().make_sound()
        print("meow meow")
class Cow(Animals):
    def make_sound(self):
        super().make_sound()
        print("cow cow")
x=[Dog(),Cow(),Cat()]
for i in x:
    i.make_sound()









# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.
# Q3. Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.
# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.
# Q5. Using the abc module, create an abstract class Notification with send().
# Implement subclasses EmailNotification, SMSNotification, PushNotification — each
# with its own send() logic.
# Demonstrate polymorphism by looping over all and calling send().
# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.
# Q7. Create:
# • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
# each implementing a different logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using
# interchangeable strategy objects.
# Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.
# Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
# Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?
# Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
# pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling
# pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.









#4.Design an Employee class where:
#• salary is hidden
#• outsiders cannot read salary directly
#• use getter method that logs each access attempt
#• provide a method to update salary but only if the new salary is higher (prevent
#accidental downgrade)

class Employee:
    def __init__(self,s):
        self.__s=s
        self.__log=[]
    def getter(self):
        self.__log.append("accessed")
        return self.__s
    def setter(self,new):
        if new>self.__s:
            self.__s=new
            print(f"salary updated {self.getter()} to {new}")
        else:
            print("salary is decresed")
    def show(self):
        return self.__log
e=Employee(4000)
e.getter()
e.setter(5000)
print(e.show())


#7. Create:
#• An Engine class with private state like temperature
#• A Car class that uses an Engine but should:
#o Not allow users to manipulate engine temperature
#o Only expose methods like start_car() or cool_engine()
#Demonstrate why giving direct engine access is dangerous.



class Engin:
    def __init__(self,a):
        self.__a=a
    def getter(self):
        return self.__a
class Car(Engin):
    def __init__(self,b):
        super().__init__(b)
    def start_car(self):
        self.b=self.getter()+20
        return self.b

    def cool(self):
        self.b-=15
        return self.b
c=Car(20)
print(c.start_car())
print(c.cool())
