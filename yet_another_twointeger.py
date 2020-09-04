#https://codeforces.com/contest/1409/problem/A
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>y:
        r=x-y
        r=r//10
        if x-r*10!=y:
            r+=1
        print(r)
    else:
        r=y-x
        r=r//10
        if x+r*10!=y:
            r+=1
        print(r)
    