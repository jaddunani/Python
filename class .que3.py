n=int(input())
a=[]
c=[]
d=[]
for i in range(1,2*n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
          count+=1
    if count==2:
        a.append(i)
#print(a)
b=len(a)
#print(b)
for j in range(b):
    if n<=a[j]:
        c.append(a[j])
    else:
        d.append(a[j])
#print(c)
#print(d)
q=c[0]
#print(q)
w=d[-1]
#print(w)
s=q-n
t=n-w
if s<t:
    if q==n:
        print(c[1])
    else:
        print(q)
elif t<s:
        print(w)
else:
    print(q,w)





