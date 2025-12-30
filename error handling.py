#• Create a class Person whose constructor takes age as an argument. Raise a
#ValueError if the age is less than 0.
#from importlib.metadata import pass_none

# class Person:
#     def __init__(self,age):
#         if age<=0:
#             raise ValueError("pass age is not eligible")
#         else:
#             print(age)
#         self.age=age
# try:
#
#     p=Person(-1)
# except Exception as e:
#     print(e)


#• Write a function named find_length(obj) that uses a loop to calculate the
#length of the given object without using the built-in len() function. The
#function should return the calculated length if the object is iterable. If a
#non-iterable object such as an integer is passed, the function should raise and
#handle a TypeError, and print an appropriate error message explaining what
#happens when an integer is sent as input.
#
# def findlength(obj):
#     try:
#         c=0
#         for i in obj:
#             c+=1
#         return c
#     except TypeError as e:
#         print("invalid input",e)
# print(findlength("njwcnj"))
# print(findlength(45))



#• Create a class Student with an attribute marks. Implement a method
#set_marks(marks) that raises a ValueError if marks are not in the range 0 to
#100.

# class Student:
#     #def __int__(self,marks):
#         #self.marks=marks
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.marks=marks
#             print(self.marks)
#         else:
#             raise ValueError("entered marks are not in given range")
# try:
#     s=Student()
#     s.set_marks(101)
# except Exception as e:
#     print(e)


#• Create a custom exception named InvalidAgeError. Create a class Voter with a
#method check_eligibility(age) that raises this exception if age is less than 18.

# class InvalidAgeError(Exception):
#     pass
# class Voter:
#     def check_eligibility(self,age):
#         if age<18:
#             raise InvalidAgeError("your age is not eligibile for voting")
#         else:
#             print(age)
# try:
#     v=Voter()
#     v.check_eligibility(12)
# except Exception as e:
#     print(e)



#• Create a class BankAccount with an attribute balance. Implement a method
#withdraw(amount) that raises an exception if the withdrawal amount is greater
#than the available balance.


# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount>=self.balance:
#             raise Exception("no sufficient balnce ")
#         else:
#             print(f"balance={self.balance-amount}")
# try:
#     b=BankAccount(2000)
#     b.withdraw(2001)
# except Exception as e:
#     print(e)


#• Create a class PasswordValidator with a method validate(password). Raise an
#exception if the password length is less than 8 characters.

# class PasswordValidator:
#     def validate(self,password):
#         c=0
#         for i in password:
#             c+=1
#         if c<8:
#             raise Exception("your password should be more than 8 characters")
#         else:
#             print(password)
# try:
#     p=PasswordValidator()
#     p.validate("jcjw")
# except Exception as e:
#     print(e)


#• Create a class UserInput with a method get_integer(value). Handle ValueError
#and TypeError using separate except blocks.

# class UserInput:
#     def get_integer(self,value):
#         try:
#             result=int(value)
#             print(result)
#         except TypeError as e:
#             print("given input is not an int value",e)
#         except ValueError as e:
#             print("given input is not in given range",e)
# u=UserInput()
# u.get_integer("hs")

#• Create a base class Shape with a method area() that raises
#NotImplementedError. Create a child class Rectangle that overrides and
#implements the area method.


# class Shape:
#     def area(self):
#         raise NotImplementedError("not implemented")
# class Rectangle(Shape):
#     def area(self):
#         print("area")
#         super().area()
# try:
#     r=Rectangle()
#     r.area()
# except Exception as e:
#     print(e)



#• Create a class Service with a method that calls another method which raises an
#exception. Catch and handle the exception in the Service class.


# class Service:
#     def m1(self):
#         raise Exception("error")
#     def m2(self):
#         try:
#             self.m1()
#         except Exception:
#             print("expection error")
# s=Service()
# print(s.m2())


#• Create a class Transaction with a method process() that uses try, except, and
#finally blocks to ensure a cleanup message is always printed.


# class Transcation:
#     def process(self):
#         try:
#             print("process Strated")
#             result=int("ab")
#             print("sucessfully processed")
#         except ValueError as e:
#             print("value error",e)
#         finally:
#             print("transtion completed")
# t=Transcation()
# t.process()


#• Create a class LoginSystem with a method login(password) that raises an
#exception for an incorrect password and handles the exception outside the class.


class LoginSystem:
    def __init__(self,passw):
        self.__passw=passw
    #@property
    #def p1(self):
        #return self.__passw
    def login(self,password):
        if self.__passw!=password:
            raise Exception("entered password is incorect")
        else:
            print("login succesfully")
try:
    l=LoginSystem("suvarna")
    l.login("suvarna")
except Exception as e:
    print(e)






