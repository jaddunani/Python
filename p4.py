#Q10. Create a class Student with:
#•	class variable passing_marks = 40
#•	instance attributes name, marks
#•	instance method result() → prints pass/fail using class variable
#•	class method update_passing_marks(cls, new_marks)
#•	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
#Use all three in a program that:
#1.	Creates students
#2.	Updates the passing criteria
#3.	Displays grade category and result

class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>self.passing_marks:

            print("pass")
            return
        print("fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=90:
            print("A")
        elif 80<=marks<=89:
            print("B")
        else:
            print("C")
M1=Student("jaddu",65)
M2=Student("pavan",34)
M3=Student("anurag",41)
M1.result()
M2.result()
M1.update_passing_marks(45)
M3.result()
M2.grade_category(2)
