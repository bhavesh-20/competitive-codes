#https://codeforces.com/problemset/problem/261/A
nq=int(input())
q=[int(x) for x in input().split()]
n=int(input())
a=[int(x) for x in input().split()]
a.sort(reverse=True)
m=min(q)
i=0
ans=0
x=0
while i<n:
    if x==m:
        x=0
        i+=2
        continue
    x+=1 
    ans+=a[i]
    i+=1
print(ans)
