class Shape:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        raise NotImplementedError("not implemented error")
    def validate(self,num):
        if num<0:
            raise TypeError("num is Type error taken")
        else:
            print(num)
class Rectangle(Shape):
    def area(self):
        area=self.a*self.b
        if area>0:
            return area
        else:
            super().validate(area)
    def m1(self):
        try:
            super().validate(self.area())
        except Exception as e:
            print(e)
        finally:
            print("shapes as some area")
try:
    r=Rectangle(-1,2)
    r.m1()
except Exception as  e:
    print(e)

