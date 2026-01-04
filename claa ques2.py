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

# s=int(input())
# e=int(input())
# if s>e:
#     print("invalid numbers")
# else:
#     sum=0
#     count=0
#     for i in range(s,e+1):
#         if i%2==0:
#             print(i,end=" ")
#             sum+=i
#             count+=1
#     print(sum)
#     if count==0:
#         print("no even numbers")


# n=int(input())
# a=[]
# c=[]
# d=[]
# for i in range(1,2*n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#           count+=1
#     if count==2:
#         a.append(i)
# #print(a)
# b=len(a)
# #print(b)
# for j in range(b):
#     if n<=a[j]:
#         c.append(a[j])
#     else:
#         d.append(a[j])
# #print(c)
# #print(d)
# q=c[0]
# #print(q)
# w=d[-1]
# #print(w)
# s=q-n
# t=n-w
# if s<t:
#     if q==n:
#         print(c[1])
#     else:
#         print(q)
# elif t<s:
#         print(w)
# else:
#     print(q,w)

# n=int(input())
# min=n
# while n>0:
#     r=n%10
#     if min>r:
#         min=r
#     n=n//10
# print(min)

#
# n=int(input())
# s=n**2
# l=len(str(n))
# rev=0
# while l>0:
#     r=s%10
#     rev=rev*10+r
#     s=s//10
#     l-=1
# print(rev)
# f=0
# while rev>0:
#     r=rev%10
#     f=f*10+r
#     rev=rev//10
# print(f)
# if n==f:
#     print("auto")
# else:
#     print("no")


x=[1,2]
y=x
x=x.append(3)
print(y)


