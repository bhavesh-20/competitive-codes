n,m=list(map(int,input().split()))
a=[]
for _ in range(n):
    a.append(list(input()))
b=list(zip(*a))
ans=[]
for i in range(n):
    for j in range(m):
        c1=len(set(a[i]))
        c2=len(set(a[i][:j]+a[i][j+1:]))
        c3=len(set(b[j]))
        c4=len(set(b[j][:i]+b[j][i+1:]))
        if c1==c2+1 and c3==c4+1:
            ans.append(a[i][j])
ans=''.join(x for x in ans)
print(ans)