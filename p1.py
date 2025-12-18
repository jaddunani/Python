#Q7. Create a class Employee with:
#•	instance attributes: name, base_salary
#•	class variable: bonus_rate = 0.1
#•	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
#•	class method: update_bonus(cls, new_rate) → updates bonus for all employees
#•	static method: is_valid_salary(sal) → checks if salary > 0


class Employee:
    b_r=0.1
    def __init__(self,name,bs):
        self.name=name
        self.bs=bs
    def final_salary(self):
        return self.bs+(self.bs*self.b_r)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.b_r=new_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            return True
        return False
o1=Employee("jaddu",10000)
print(o1.b_r)
print(o1.final_salary())
Employee.update_bonus(0.3)
print(o1.b_r)
print(o1.final_salary())
print(o1.is_valid_salary(o1.final_salary()))

