def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a

n,m=map(int,input().split())

a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

ans=[]

if n==1:
    for i in range(m):
        ans.append(a[0]+b[i])
else:
    a.sort()
    for i in range(1,n):
        a[i]-=a[0]
    result=a[1]
    for i in range(2,n):
        result=gcd(result,a[i])
        if result==1:
            break
    for i in range(m):
        ans.append(gcd(result,b[i]+a[0]))
for i in ans:
    print(i,end=' ')
print(" ")