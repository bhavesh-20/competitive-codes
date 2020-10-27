#https://codeforces.com/contest/1437/problem/A
for _ in range(int(input())):
    l,r=map(int,input().split())
    ans=2*l
    if r%ans==r:
        print("YES")
    else:
        print("NO")