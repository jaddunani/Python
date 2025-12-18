#Q9. Create a class BankAccount with:
#•	class variable bank_name
#•	instance variables holder and balance
#•	instance method deposit(amount)
#•	class method change_bank_name(cls, new_name)
#•	static method validate_amount(amount) → returns True if amount > 0


class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank=new_name
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        return False
A1=BankAccount("jaddu",1000)
A2=BankAccount("pavan",10000)
A3=BankAccount("anurag",100000)
A1.deposite(10000)
A2.deposite(20000)
A3.deposite(30000)
print(A1.balance)
print(A2.balance)
print(A3.balance)
A1.change_bank_name("bob")
print(A2.bank_name)
print(A3.validate_amount(A3.balance))

