# def isprime(num):
#     c=0
#     for i in range(1,int(num**0.5)+1):
#         if num%i==0:
#             c+=1
#     if c==1:
#         return True
# n=list(map(int,input().split()))
# for i in n:
#     if isprime(i):
#         print(i,end=" ")

# n=list(map(int,input().split()))
# r=int(input())
# sum=0
# for i in range(r):
#     sum+=n[i]
# print(sum)

# n=list(map(int,input().split()))
# for i in n:
#     a=1
#     b=2
#     for j in range(0,i+1):
#         if i==a:
#             print(i)
#             break
#         elif a>i:
#             break
#         c=a+b
#         a=b
#         b=c

# n=list(map(int,input().split()))
# max=0
# min=0
# for i in n:
#     a=0
#     b=1
#     while True:
#         if i==b:
#             pass
#         elif b>i:
#             if b==i:
#                 max=c
#             else:
#                 max=b
#             if a==i:
#                 min=b-a
#             else:
#                 min=a
#             break
#         c=a+b
#         a=b
#         b=c
#     print(min,i,max,end=" =")
#     if i-min>max-i:
#         print(max)
#     elif i-min<max-i:
#         print(min)
#     else:
#         print(min,max)
#     print()


# l=list(map(int,input().split()))
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# c=0
# while c<4:
#     if min in l:
#         pass
#     else:
#         print(min)
#         c+=1
#     min+=1


# l=list(map(int,input().split()))
# n=int(input())
# for i in range(1,n+2):
#     if i in l:
#         pass
#     else:
#         print(i)