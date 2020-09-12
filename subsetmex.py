#https://codeforces.com/contest/1406/problem/A
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    s1=set()
    s2=set()
    for i in a:
        if i not in s1:
            s1.add(i)
        elif i not in s2:
            s2.add(i)

    c=0
    for i in s1:
        if i!=c:
            break
        else:
            c+=1

    c2=0

    for i in s2:
        if i!=c2:
            break
        else:
            c2+=1
    print(c+c2)