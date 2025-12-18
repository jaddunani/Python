def fun(n):
    if n%11==0:
        return True
    else:
        return False
n=int(input())
if fun(n):
    print("yes")
else:
    print("no")