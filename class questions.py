s=int(input())
e=int(input())
if s>e:
    print("wrong number")
else:
    for i in range(s,e+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i,end=" ")

