#https://codeforces.com/contest/1497/problem/B
for _ in range(int(input())):
    n,m = map(int,input().split())
    a = [int(x) for x in input().split()]
    d = dict()
    for i in range(m):
        d[i] = 0
    for i in a:
        d[i%m]+=1
    s = (1 if d[0]!=0 else 0)
    if m%2==0:
        s = ((s+1) if d[m//2]!=0 else s)
    for i in range(1,(m-1)//2+1):
        x = min(d[i],d[m-i])
        if x!=0:
            s+=1
            x+=1
        d[i]-=x
        d[m-i]-=x
        
        if d[i]>0:
            s+=d[i]
        if d[m-i]>0:
            s+=d[m-i]
    print(s)
