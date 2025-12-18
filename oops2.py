#1. Create a BankAccount class that stores:
#• account number
#• balance (should not be directly modifiable)
#You must:
#1. Make the balance attribute inaccessible from outside.
#2. Provide functions to deposit/withdraw that validate the amount.
#3. Prevent withdrawal if balance becomes negative.
#4. Show what happens if someone tries to modify balance directly and why
#encapsulation prevents it.


class BankAccount:
    def __init__(self,an,b):
        self.account_number=an
        self.__b=b
    def getter(self):
        return self.__b
    def setter(self,new):
        self.__b=new
    def deposit(self,amount):
        print(f"{self.getter()+amount}")
    def withdrawal(self,amount):
        if self.getter() and self.getter()>=amount:
            print(f"{self.getter()-amount}")
        else:
            print("Invalid balance")
c1=BankAccount(2314,20000)
c2=BankAccount(3456,2000)
print(c1.getter())
c1.setter(20000)
c1.deposit(2000)
c1.withdrawal(2000)


#2. Design a Student class where marks:
#• should always be between 0 and 100
#• should never be set directly
#Enable updating marks only through a controlled method that performs range
#checks.
#Demonstrate:
#• trying to assign marks manually
#• why encapsulation protects invalid states


class Student:
    def __init__(self,marks):
        self.__marks=marks
    def gettre(self):
        return self.__marks
    def setter(self,new):
        if 0<=new<=100:
            self.__marks=new
        else:
            return "Invalid marks"
s=Student(34)
print(s.gettre())
print(s.setter(100))
print(s.gettre())



#3. Create a SecureFile class that:
#• stores content privately
#• provides a method read(password)
#• refuses access if the password is incorrect
#• logs an "Unauthorized attempt" internally (cannot be accessed from outside

class SecureFile:
    def __init__(self,p):
        self.__p=p
        self.__log=[]
    def getter(self):
        return self.__p
    def read(self,password):
        if self.getter()!=password:
            self.__log.append("Unauthorized attempt")
        else:
            print("authorized attempt")
    def _show_log(self):
        return self.__log
f=SecureFile(345)
print(f.getter())
f.read(342)
print(f._show_log())

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
            print(f"salary updated {self.__s} to {new}")
        else:
            print("salary is decresed")
    def show(self):
        return self.__log
e=Employee(4000)
e.getter()
e.setter(5000)
print(e.show())


#5. Create a Product class where:
#• price cannot be negative
#• discount cannot exceed 70%
#• internal final price calculation should not be directly exposed
#Provide only one public method get_final_price().

class Product:
    def __init__(self):
        self.__price = 0
        self.__discount = 0
    def __calculate_final_price(self):
        return self.__price * (1 - self.__discount / 100)
    def set_price(self, price):
        if price < 0:
            print("Invalid price! Price cannot be negative.")
        else:
            self.__price = price
    def set_discount(self, discount):
        if discount < 0 or discount > 70:
            print("Invalid discount! Must be between 0% and 70%.")
        else:
            self.__discount = discount
    def get_final_price(self):
        return self.__calculate_final_price()

p=Product()
p.set_price(45)
p.set_discount(30)
print(p.get_final_price())


#6. Create a Character class with:
#• private _health
#• methods to damage(points) and heal(points)
#• health cannot drop below 0 or exceed max limit
#• expose only current health through a read-only getter


class Character:
    def __init__(self,health):
        self.__health=health
        self.maxhealth=100
        self.minhealth=0

    def getter(self):
        return self.__health
    def damage(self,points):
        if points>0:
            self.__health-=points
            if self.__health<0:
                return self.__health==self.minhealth
            else:

                return self.__health
        else:
            return "there is no damage"
    def heal(self,points):
        if points>0:
            self.__health+=points
            if self.__health>self.maxhealth:
                return self.__health==self.maxhealth
            else:
                return self.__health

c=Character(56)
print(c.getter())
c.damage(32)
c.heal(54)
print(c.getter())


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
        self.b=b
    def start_car(self):
        self.b=self.getter()+20
        return self.b

    def cool(self):
        self.getter-=15
        return self.__a
c=Car(20)
print(c.start_car())


#8. Create a ShoppingCart class where:
#• items are stored privately
#• users cannot directly modify item list
#• only add/remove methods are allowed
#• provide a method to get a safe copy of the cart items (not direct reference to internal
#list)

class Shoppingcart:
    def __init__(self):
        self.__log=[]
    def add(self,item):
        self.__log.append(item)
        print(f"{item}")
    def remove(self,item):
        if item in self.__log:
            self.__log.remove(item)
            print(f"{item}")
    def show(self):
        return self.__log
s=Shoppingcart()
s.add("su")
s.add("ku")
s.remove("ku")
print(s.show())











