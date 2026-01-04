
#1. Write a Python program that attempts to dynamically import a module at
#runtime. The program should only import the module if it actually exists;
#otherwise, it should print "Module does not exist".

a=10
b=20


import importlib
a=input()
try:
    x=importlib.import_module(a)
    print("a modele exist")
except Exception as e:
    print("module not exist",e)