# # #automorphic
n=int(input())
sq=n**2
print(sq)
l=len(str(n))
print(l)
rev=0
while l>0:
    r=sq%10
    rev=rev*10+r
    sq=sq//10
    l-=1
print(rev)
d=0
while rev>0:
    r=rev%10
    d=d*10+r
    rev=rev//10
print(d)
if n==d:
    print("it is automorphic")
else:
    print("its not a automorphic")



#
#
# #technumbers
n=int(input())
l=len(str(n))
l1=l/2
m=n
d=0
if l%2!=0:
    print("invalid input")
else:
    rev=0
    while l>(l1):
        r=m%10
        rev=rev*10+r
        m=m//10
        l-=1
    while rev>0:
        r=rev%10
        d=d*10+r
        rev=rev//10
    print(d)
    print(m)
    sum=d+m
    sum=sum**2
    print(sum)
    if sum==n:
        print("technumber")
    else:
        print("not a technumber")


# #spynunber

n=int(input())
m=n
sum=0
mul=1
while m>0:
    r=m%10
    sum=sum+r
    mul=mul*r
    m=m//10
print(sum)
print(mul)
if sum==mul:
    print("spynumber")
else:
    print("not a spynumber")





# #peterson
n=int(input())
m=n
sum=0
while m>0:
    r=m%10
    f=1
    for i in range(1,r+1):
        f=f*i
    print(f)
    sum+=f
    m=m//10
print(sum)
if sum==n:
    print("preterson")
else:
    print("not peterson")



