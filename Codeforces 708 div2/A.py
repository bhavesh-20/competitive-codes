#https://codeforces.com/contest/1497/problem/0
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = dict()
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=0
    b = list(sorted(set(a)))
    for i in d:
        if d[i]>0:
            l = [i]*d[i]
            b.extend(l)
    for i in b:
        print(i,end=' ')
    print('')
    