#1. Write a Python program that attempts to dynamically import a module at
#runtime. The program should only import the module if it actually exists;
#otherwise, it should print "Module does not exist".
import sys
a=input()
if a in sys.modules:
    print(a)
else:
    print("module not found")


# import importlib
# a=input()
# try:
#     x=importlib.import_module(a)
#     print("found")
# except Exception as e:
#     print("module not found",e)


