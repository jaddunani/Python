# 1. Design a banking system with:
# • An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must:
# o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies.
# Demonstrate:
# • Polymorphic behavior by iterating through all account types
# • Preventing direct access to balance
# • Multiple interest strategies

class Account:
    interest=1.6
    def __init__(self,b):
        self.__balance=b
    def m1(self):
        return self.__balance
    def m2(self,new):
        self.__balance=new
    def deposit(self,amount):
        self.m1=self.m1()+amount
        return self.m1()
    def withdraw(self,amount):
        self.m1-=amount
        return self.m1()
    def claculate_interest(self,amount):
        cal=amount*self.interest
        return cal
    @classmethod
    def change(cls,new_i):
        cls.interest=new_i


