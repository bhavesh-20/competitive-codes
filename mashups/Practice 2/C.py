n,k,t=map(int,input().split())
f=(t*n*k)//100
x=f//k
r=f%k
a=[]
for i in range(n):
    if i<x:
        a.append(k)
    elif i==x:
        a.append(r)
    else:
        a.append(0)
for i in a:
    print(i,end=' ')