s=int(input())
e=int(input())
if s>e:
    print("invalid numbers")
else:
    sum=0
    count=0
    for i in range(s,e+1):
        if i%2==0:
            print(i,end=" ")
            sum+=i
            count+=1
    print(sum)
    if count==0:
        print("no even numbers")
