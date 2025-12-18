# # n=int(input())
# # for i in range(1, n + 1):
# #     for j in range(1, i + 1):
# #         print(chr(65 + n - j), end=" ")
# #     print()
# # '''
# # 5
# # E
# # E D
# # E D C
# # E D C B
# # E D C B A
# # '''
#
# #
# def isprime(num):
#     c=0
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             c+=1
#     if c==0:
#         return True
# n=int(input())7
# for i in range(1,n+1):
#     c=1
#     for j in range(1,i+1):
#         while True:
#             c+=1
#             if isprime(c):
#                 print(c,end=" ")
#                 break
#     print()
# #
#
#
# def isprime(num):
#     c=0
#     for i in range(1,num+1):
#         if num%i==0:
#             c+=1
#     if c==2:
#         return True
# n=int(input())
# m=1
# c=1
# while c<=n:
#     while True:
#         m+=1
#         if isprime(m):
#             c+=1
#             print(m)
#             break

#
# n=int(input())
# c=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c+=2
#     c-=1
#     print()


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=i:
            print(n-i+1,end=" ")
        else:
            print(n-j+1,end=" ")
    for k in range(1,n):
        if j>=i:
            print(n-i+j+1,end=" ")
        else:
            print(n-j+1,end=" ")
    print()
