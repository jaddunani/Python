#• Write a Python program using a context manager (with) to open a text file in
#read mode, read the entire content using read(), and print the number of
#characters in the file.

with open("s.txt","r") as f:
    context=f.read()
print(context)
print(len(context))

#• Write a program that opens a file using a context manager, reads all lines
#using readlines(), and prints only the lines that contain more than 10
#characters.

with open("s.txt","r") as f:
    context=f.readlines()
for i in context:
    if len(i)>10:
        print(i,end="")


#• Write a program that creates a file and writes 3 lines using write(), reopens
#the same file in append mode, appends 2 more lines, and finally reads and prints
#the complete file content.
#
with open("w.txt","w") as f:
    context=[f.write("hi\n"),f.write("hello\n"),f.write("bye\n")]
print(context)
with open("w.txt","a") as f1:
    c=f1.write("hello\n"),f1.write("okk")




#• Write a program that opens a file in read mode, reads the first 10 characters,
#prints the current cursor position using tell(), moves the cursor back to the
#beginning using seek(0), and reads the full content again.

f=open("s.txt","r")
print(f.read(10))
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read())


#• Create a custom context manager using a class that opens a file in write mode
#in the __enter__ method, writes a line to the file, closes the file in the
#__exit__ method, and properly prints or logs any exception information received
#in __exit__.


class Contextmanager:
    def __init__(self,filename):
        self.filename=filename
        self.file=None
    def __enter__(self):
        self.file=open(self.filename,"w")
        self.file.write("file is open in enter method\n")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(" ")
            print(exc_val)
            print(exc_tb)
        return True
with Contextmanager("m.txt") as f:
    f.write("working")

#• Create a custom context manager using @contextmanager from the contextlib
#module that opens a file, yields the file object, and ensures the file is closed
#even if an exception occurs.
#
from contextlib import contextmanager
@contextmanager
def fileopen(filename,mode):
    f=open(filename,mode)
    try:
        yield f
    finally:
        f.close()
with fileopen("m.txt","r") as e:
    print(e.read())


#• Write a program using a context manager that opens a file in read mode, uses a
#loop to read the file in small chunks (for example, 5 characters at a time),
#prints the cursor position after each read using tell(), uses seek() to move to
#a specific position, and continues reading from there.

with open("s.txt","r") as f:
    while True:
        context=f.read(5)
        if not context:
            break
        print(context)
        print(f.tell())
    f.seek(18)
    while True:
        context=f.read(5)
        if not context:
            break
        print(context)
        print(f.tell())





# #banking System
#
# import os
# filename="account.txt"
#
#
#
# with open(filename,"w") as f:
#     f.write(str(1000))
#     def check_balance():
#         with open(filename,"r") as f:
#             return int(f.read())
#
#     def show_balance(balance):
#         with open(filename,"w") as f:
#             f.write(str(balance))
#
#     def deposite():
#         amount=int(input())
#         balance=check_balance()
#         balance+=amount
#         show_balance(balance)
#         print(balance)
#
#     def withdraw():
#         amount = int(input("Enter amount to withdraw: "))
#         balance = check_balance()
#         if amount <= balance:
#             balance -= amount
#             show_balance(balance)
#             print("Withdrawal successful")
#         else:
#             print("Insufficient balance")
#         print("Current Balance:", balance)
# while True:
#     print("\n--- Banking System ---")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")
#
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         deposite()
#     elif choice == "2":
#         withdraw()
#     elif choice == "3":
#         print(check_balance())
#     elif choice == "4":
#         print("Thank you for using the banking system")
#         break
#     else:
#         print("Invalid choice")
#


import os
from random import choice

filename="account1.txt"
if not os.path.exists(filename):
    with open(filename,"w") as f:
        f.write("1000")
def show_balance():
    with open(filename,"r") as f:
        return int(f.read())
def write_balance(balance):
    with open(filename,"w") as f:
        f.write(str(balance))
def deposite():
    amount=int(input())
    balance=show_balance()
    balance+=amount
    write_balance(balance)
    print(balance)
def withdraw():
    amount=int(input())
    balance=show_balance()
    if amount<=balance:
        balance-=amount
        write_balance(balance)
    else:
        print("insufficint amount")
    print(balance)

while True:
    print("1.show_balance")
    print("2.deposite")
    print("3.withdraw")
    print("4.exit")

    choice=input("enter your choice")

    if choice=="1":
        print(show_balance())
    elif choice=="2":
        deposite()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        print("thanks for visting us")
        break
    else:
        print("Invalid choice")



