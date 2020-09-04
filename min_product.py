#https://codeforces.com/contest/1409/problem/B
for _ in range(int(input())):
    a,b,x,y,n=map(int,input().split())
    l=[[a,x],[b,y]]
    r=[[a,x],[b,y]]
    r.reverse()
    temp=n
    for i in l:
        m=min(n,i[0]-i[1])
        n-=m
        i[0]-=m
    mi=l[0][0]*l[1][0]
    n=temp
    for j in r:
        m=min(n,j[0]-j[1])
        n-=m
        j[0]-=m
    mi=min(mi,r[0][0]*r[1][0])
    print(mi)