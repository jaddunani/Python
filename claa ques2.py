'''
n=int(input("enter no."))
for i in range(1,n+1):
    if i%3==1:
        print("#",end=" ")
    elif i%3==2:
        print("@",end=" ")
    else:
        print("$",end=" ")
'''

n=int(input())
max=n
while n>0:
    r=n%10
    if max>r:
        max=r
    n=n//10
print(max)
