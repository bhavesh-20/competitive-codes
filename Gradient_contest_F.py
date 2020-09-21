#https://codeforces.com/gym/294377/problem/F
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    a=a[:]+a[:]
    m=0
    sum=0
    n=len(a)
    for i in range(k):
        sum+=a[i]
    for i in range(k,n):
        sum+=a[i]
        sum-=a[i-k]
        m=max(sum,m)
    print(m)