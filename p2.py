#Q8. Create a class Course with:
#•	class variable total_students
#•	instance variable student_name
#•	instance method enroll() → increments total_students
#•	class method show_total(cls) → prints total students
#•	static method is_eligible(age) → returns True if age ≥ 18


class Course:
    total_students=0
    def __init__(self,name):
        self.name=name
    def enroll(self):
        self.total_students=self.total_students+1
    @classmethod
    def show_total(cls):
        return cls.total_students
    @staticmethod
    def is_eligible(age):
        if age>=18:
            return True
        return False
o1=Course("A1")
o2=Course("A2")
o1.enroll()
o1.enroll()
print(o1.total_students)
print(o1.show_total())









