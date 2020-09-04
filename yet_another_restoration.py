#https://codeforces.com/contest/1409/problem/C
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    m=100000000000
    for i in range(1,n):
        if (y-x)%i==0:
            diff=(y-x)//i;
        m=min(m,diff)
    diff=m
    a=[x,y]
    for i in range(x+diff,y,diff):
        if len(a)==n:
            break
        a.append(i)
    if len(a)<n:
        m=min((x-1)//diff,n-len(a)) 
        temp=x-diff
        for i in range(m):
            a.append(temp)
            temp-=diff
    if len(a)<n:
        i=y+diff
        while True:
            if len(a)==n:
                break
            a.append(i)
            i+=diff
    for i in a:
        print(i,end=' ')
    print('')