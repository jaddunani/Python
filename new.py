s=int(input())
e=int(input())
if s>e:
    print("invalid numbers")
else:
    sum=0
    for i in range(s,e+1):
        sum+=i
    print(sum)
