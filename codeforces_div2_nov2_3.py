#https://codeforces.com/contest/1443/problem/C
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    pick=0
    delivery=0
    l=[]
    for i in range(n):
        l.append([a[i],b[i]])
    l.sort(reverse=True)
    a=[]
    b=[]
    for i in range(n):
        a.append(l[i][0])
        b.append(l[i][1])
    for i in range(n):
        if pick+b[i]<a[i]:
            pick=pick+b[i]
        else:
            delivery=max(delivery,a[i])
    print(max(pick,delivery))
