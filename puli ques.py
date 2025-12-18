'''
n=int(input())
sum=1
for i in range(0,n):
    sum+=i
    print(sum,end=" ")

n=int(input())
c=0
for i in range(1,n+1):
    c+=1
    if c>1:
        print(",",end=" ")
    if i%2==0 and i%3==0:
        print("fizz buzz",end="")
    elif i%2==0:
        print("fizz",end="")
    elif i%3==0:
        print("buzz",end="")
    else:
        print(i,end="")
'''
from pratice import count

''''
n=int(input())
c=0
for i in range(1,n+1):
    if 2**i==n:
        c+=1
if c==1:
    print('yes')
else:
    print("no")
'''
'''
def prime(num):
    for i in range(2,num+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            print(i)
prime(10)
'''
'''
class Employee:
    br=0.1
    def __init__(self,name,bs):
        self.name=name
        self.bs=bs
    def final_salary(self):
        return self.bs + (self.bs*self.br)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.br=new_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            return True
        return False
E1=Employee("jaddu",10000)
E2=Employee("pavan",20000)
print(E1.final_salary())
print(E2.final_salary())
E1.update_bonus(3)
print(Employee.br)
print(E2.is_valid_salary(E2.final_salary()))
'''
class Employee:
    emp_count = 0   # class variable

    def __init__(self, name):
        self.name = name
    def count(self):
        self.emp_count+=1
    def get_count(self):
        return count()



e1 = Employee("A")
e2 = Employee("B")
e3 = Employee("C")
print(Employee.get_count())

