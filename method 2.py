#Q1. Create a class Student that:
#•	Keeps track of the total number of students created.
#•	Determines whether a student passed or failed based on a shared passing mark.
#•	Provides a method to curve marks by increasing everyone’s marks by a percentage.
#•	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
#Demonstrate:
#1.	Creating multiple students.
#2.	Applying a grading curve.
#3.	Displaying updated results with letter grades.
#from ctypes import HRESULT


class Student:
    total_students=0
    passing_mark=40
    percentage=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.total_students+=1
    def passed(self):
        if self.marks>self.passing_mark:
            return "passed"
        return "failed"
    def c_m(self):
        self.marks+=(self.marks*self.percentage)
        return self.marks
    @classmethod
    def update(cls,new_percentage):
        cls.percentage=new_percentage
    @staticmethod
    def updated_result(m):
        if 91<=m<=100:
            return "A"
        elif 81<=m<=90:
            return "B"
        else:
            return "C"
S1=Student("jaddu",56)
S2=Student("pavan",87)
print(S1.passed())
print(S1.marks)
S2.update(0.5)
print(S1.c_m())
print(S1.updated_result(S2.marks))



#Q2. Design a class Product that:
#•	Maintains a base tax rate applicable to all products.
#•	Each product has a name and base price.
#•	Has a method to compute final price including tax.
#•	Can change tax rate for all products using one method.
#•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
#Demonstrate:
#1.	Creating multiple products.
#2.	Changing the tax rate.
#3.	Showing updated prices and validity checks.


class Product:
    base_tax=0.11
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        self.base_price+=(self.base_price*self.base_tax)
        return self.base_price
    @classmethod
    def changetax(cls,new_tax):
        cls.base_tax=new_tax
    @staticmethod
    def function(price):
        if price<0:
            return "invalid"
        return "valid"
p1=Product("n",200)
p2=Product("s",400)
print(p1.final_price())
p2.changetax(0.15)
print(p1.final_price())
print(p2.function(p2.base_price))

'''

#Q3. Create an Employee class that:
#•	Keeps a minimum experience required for promotion (shared across all employees).
#•	Stores employee name, experience, and department.
#•	Has a method to check eligibility for promotion.
#•	Provides a function to update promotion criteria globally.
#•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
#Demonstrate:
#1.	Creating employees from different departments.
#2.	Changing promotion criteria.
#3.	Displaying eligibility results and department validation.

'''
class Employee:
    minimum_exp=0
    def __init__(self,name,exp,dep):
        self.name=name
        self.exp=exp
        self.dep=dep
    def eligibility(self):
        if self.exp>=self.minimum_exp:
            return "eligible"
        return "Not eligible"
    @classmethod
    def update(cls,new_exp):
        cls.minimum_exp=new_exp
    @staticmethod
    def department(dep):
        if dep=="Hr" or dep=="tech" or dep=="admin":
            return "valid"
        return "invalid"
c1=Employee("jaddu",3,"tech")
c2=Employee("nikhil",1,"traine")
c1.update(2)
print(c2.eligibility())
print(c2.department(c2.dep))

'''

#Q4. Build a Loan class that:
#•	Has a common interest rate for all loans.
#•	Each object stores borrower name and principal.
#•	Calculates total payable amount.
#•	Provides a function to update the interest rate.
#•	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
#Demonstrate:
#1.	Creating multiple loan accounts.
#2.	Updating interest rates.
#3.	Checking eligibility and total repayment for borrowers.

'''
class Loan:
    interest_rate=0.1
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    def total_payble_amount(self):
        self.amount+=(self.amount*self.interest_rate)
        return self.amount
    @classmethod
    def update(cls,new_interest):
        cls.interest_rate=new_interest
    @staticmethod
    def check(amount):
        if 50000<=amount:
            return "eligible"
        return "not eligible"

l1=Loan("jaddu",30000)
l2=Loan("nikhil",50000)
print(l2.total_payble_amount())
l1.update(0.5)
print(l2.total_payble_amount())


'''
Q5. Create a class Course that:
•	Tracks total courses created.
•	Each course has a title, duration, and enrolled_students.
•	Provides a method to enroll a new student.
•	Allows updating the minimum duration for a valid course across all instances.
•	Has a static function to check if a given duration is realistic (not negative, not too large).
Demonstrate:
1.	Creating multiple courses.
2.	Enrolling students.
3.	Updating minimum duration and checking durations.
'''

class Course:
    total_course=0
    min_duration=0
    def __init__(self,tittle,duration):
        self.tittle=tittle
        self.duration=duration
        self.enrolled_students=[]
        Course.total_course+=1
    def enroll_student(self, student_name):
        """Enroll a new student into the course"""
        self.enrolled_students.append(student_name)
        print(f"{student_name} enrolled in '{self.tittle}'")
    @classmethod
    def duration(cls,new_dur):
        cls.min_duration=new_dur

    def is_realistic_duration(duration):
        """Static method to check if duration is realistic"""
        if duration <= 0:
            return "Unrealistic (<= 0)"
        elif duration > 60:
            return "Unrealistic (> 60 months)"
        else:
            return "Realistic"
c1=Course("A",2)
c2=Course("B",3)
print(c1.tittle)
c1.enroll_student("jaddu")
c2.enroll_student("kumar")



#Q6. Design a class Vehicle that:
#•	Keeps a record of service charge rate common to all vehicles.
#•	Each vehicle has a model, kilometers_run, and service history.
#•	Has a function to calculate service charge based on km and rate.
#•	Provides a method to update the service rate for all vehicles.
#•	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
#Demonstrate:
#1.	Creating vehicles with different km and models.
#2.	Updating the service rate.
#3.	Showing charges and eligibility checks.
class Vehicle:
    service_charge_rate=40
    def __init__(self,model,kilo_run,service_his):
        self.model=model
        self.kilo_run=kilo_run
        self.service_his=service_his
    def calculation(self):
        service_charge=(self.kilo_run)*(self.service_charge_rate)
        return service_charge
    @classmethod
    def update(cls,new_rate):
        cls.service_charge_rate=new_rate
    @staticmethod
    def check(servic_his):
        if servic_his<=15:
            print("eligible")
        else:
            print("ineligible")
v1=Vehicle("a",600,20)
v2=Vehicle("b",200,10)
print(v1.calculation())
v2.update(50)
print(v1.calculation())
v2.check(v2.service_his)


#Q7. Build an Inventory class that:
#•	Tracks the total number of items across all inventories.
#•	Each instance maintains its own stock dictionary ({"item": quantity}).
#•	Provides a method to add or remove stock.
#•	Allows updating a minimum stock threshold globally.
#•	Offers a static checker to verify if a stock level is below threshold.
#Demonstrate:
#1.	Managing multiple inventories.
#2.	Adjusting stock threshold.
#3.	Using static validation inside the instance logic.

class Inventory:
    total_items=0
    min_stock=1
    def __init__(self,item,quantity):
        self.item=item
        self.quantity=quantity
        Inventory.total_items+=1
    def add(self,x):
        self.quantity=self.quantity+x
        return self.quantity
    def remove(self,y):
        self.quantity=self.quantity-y
        return self.quantity
    @classmethod
    def update(cls,new):
        cls.min_stock=new
    @staticmethod
    def check(thres,quan):
        if thres>=quan:
            print("below thres")
        else:
            print("above thres")
i1=Inventory("a",3)
i2=Inventory("b",2)
i1.add(2)
i2.remove(1)
print(i1.quantity)
print(i2.quantity)
i1.update(1)
i2.check(Inventory.min_stock,i2.quantity)



















