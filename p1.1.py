"""
class Student:
    batch="p2"
    def __int__(self,name):
        self.name=name
    def change_batch(self,new_batch):
        self.batch=new_batch
o1=Student()
o2=Student()
o3=Student()
o2.change_batch("p3")
print(o2.batch)

"""

''''
n=int(input())
p=2
c=0
while c<=n:
    c1=0
    for i in range(1,p+1):
        if p%i==0:
            c1+=1
    if c1==2:
        c+=1
        print(p,end=" ")
    p+=1
'''
'''
def isprime(num):
    for i in range(1,num+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
    if c==2:
        return True
    return False
n=int(input())
p=2
c=0
while c<=n:
    if isprime(p):
        print(p)
        c+=1
    p+=1
'''

def isprime(num):
    for i in range(1,num+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
    if c==2:
        return True
    return False
n=int(input())
p=n
max=0
while p:
    if isprime(p):
        max+=p
        break
    p+=1
print(max)
m=0
q=n
while p:
    if isprime(q):
        m+=q
        break
    q-=1
print(m)
if (max-n)>(n-m):
    print(m)
elif (max-n)<(n-m):
    print(max)
else:
    print(m,n)





