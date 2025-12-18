
n=int(input("enter number"))
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1

    if count==2:
        print(i,end=",")

        '''''
        n=int(input())
        if 0<n<1000:
            if n%2==0:
                print("even")
                a=n%3
                print(a)
            else:
                print("odd")
                a=n%2
                print(a)
        else:
            print("wrong number")
        '''''


