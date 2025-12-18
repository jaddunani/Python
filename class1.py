class student:
    batch="pyhton"
    room="102"
    def __init__(self,x,y):
        self.name=x
        self.age=y
obj=student("jaddu",22)
print(obj.name)
print(obj.age)
print(obj.batch)
print(f"my name is {obj.name}, and my age is {obj.age}, and my batch is {obj.batch}")