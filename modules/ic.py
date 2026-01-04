#7. Create a module containing two classes where one uses composition and another
#uses inheritance to reuse code from a base class. Import and demonstrate the
#difference between the two approaches.


class person:
    def m1(self):
        print("hii")
class walk(person):
    def m2(self):
        super().m1()
class see:
    def __init__(self):
        self.a=person()
    def m3(self):
        return self.a.m1()
