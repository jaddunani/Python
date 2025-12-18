def isprime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    if c==2:
        return True
n=int(input())
p=1
a=0
b=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==1:
            if j%2==1:
                while True:
                    p+=1
                    if isprime(p):
                        print(p,end=" ")
                        break
            else:
                print(a,end=" ")
                s=a+b
                a=b
                b=s
        else:
            if j%2==1:
                print(a,end=" ")
                s=a+b
                a=b
                b=s
            else:
                while True:
                    p+=1
                    if isprime(p):
                        print(p,end=" ")
                        break
    print()


# #
# n=int(input())
# a=[]
# for i in range(1,200):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         a.append(i)
# for i in range(0,n):
#     d=n-1
#     c=i
#     for j in range(1,i+2):
#         print(a[c],end=" ")
#         c+=d
#         d-=1
#
#     print()


# s=int(input())
# a=1
# b=2
# for i in range(1,s+1):
#     if i==a:
#         pass
#     elif i>a:
#         c=a+b
#         a=b
#         b=c
#         if i==a:
#             pass
#         else:
#             print(i,end=" ")
#     else:
#         print(i,end=" ")
# #


# def isprime(num):
#     c=0
#     for i in range(1,int(num**0.5)+1):
#         if num%i==0:
#             c+=1
#     if c==1:
#         return True
# n=int(input())
# for i in range(1,n+1):
#     c=i
#     d=n-1
#     p=1
#     for j in range(1,i+1):
#         while c>0:
#             p+=1
#             if isprime(p):
#                 c-=1
#                 if c==0:
#                     print(p,end=" ")
#         c+=d
#         d-=1
#     print()

#
#
# def isprime(num):
#     c=0
#     for i in range(1,num+1):
#         if num%i==0:
#             c+=1
#     if c==2:
#         return True
#
#
#
# n=int(input())
# l=len(str(n))
# c=0
# for i in range(1,l+1):
#     l1=l
#     if isprime(n):
#         print(n,end=",")
#         print("yes")
#         while l1>l-1:
#             r=n%10
#             n=n//10
#             new = int(str("1" + (l - 1) * "0"))
#             n += r * new
#             l1-=1
#             c+=1
#
#     else:
#         print(n,end=",")
#         print("not")
# if c==3:
#     print("yes")
# else:
#     print("no")




