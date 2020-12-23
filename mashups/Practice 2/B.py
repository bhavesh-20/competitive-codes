def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

n=int(input())
a=[int(x) for x in input().split()]
ans=[]
ans.append(a[0])
for i in range(n-1):
    if gcd(a[i],a[i+1])==1:
        ans.append(a[i+1])
    else:
        if a[i]%2!=0 and a[i+1]%2!=0:
            ans.append(2)
        else:
            x=1
            ans.append(x)
        ans.append(a[i+1])

print(len(ans)-len(a))
for i in ans:
    print(i,end=' ')
