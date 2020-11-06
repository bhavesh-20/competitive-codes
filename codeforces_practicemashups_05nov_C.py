#https://codeforces.com/gym/302421/problem/C

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    w=list(map(int,input().split()))
    a.sort()
    pt1=n-k-1
    pt2=n-1
    w.sort()
    ans=0
    for i in range(k):
        if w[i]==1:
            ans+=(2*a[pt2])
            pt2-=1
        else:
            ans+=(a[pt2])
            pt2-=1
            pt1-=(w[i]-1)
            ans+=a[pt1+1]
    print(ans)