'''
n=int(input())
count=0
for i in range(3,n+1):
    count+=1
    if count>1:
        print(",",end=" ")
    print(i,"*",i+1,end=" ")
'''


''''
s=int(input())
e=int(input())
count=0
for i in range(s,e+1):
    a=i*(i+1)
    count+=1
    if count>1:
        print(",",end=" ")
    print(a,end=" ")

'''''''''''



'''s=int(input())
e=int(input())
count=0
for i in range(s,e+1):
    if i%2==0:
        count+=1
        if count%2==1:
            if count>1:
                print(",",end=" ")
            print(i,end=" ")'''



'''
s=int(input())
e=int(input())
count=0
sum=0
for i in range(s,e+1):
    if i%2==0:
        count+=1
        sum+=i
print(sum)
print(count)
average=sum/count
print(f"{average:.2f}")
'''

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def m2(self):
        if (self.a*self.b)%12==0:
            return True
        else:
            return False

    def __repr__(self):
        return f"A({self.a},{self.b})"
    def m1(self):
        if self.a%2==0 and self.m2:
            return True
        else:
            return False

fl=[]
l=[A(5,3),A(4,3),A(5,3),A(6,3),A(7,3)]
for i in l:
    if i.m1():
        fl.append(i)
print(fl)
