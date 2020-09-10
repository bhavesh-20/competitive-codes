#https://codeforces.com/group/fzY0kNJuh2/contest/294236/problem/A
n,m=map(int,input().split())
ma=0
mi=10000000000000000
for _ in range(m):
    l=[int(x) for x in input().split()]
    l.sort()
    ma=max(l[0],ma)
    mi=min(l[1],mi)
if m==0:
    print(n-1)
else:
    print(max(0,mi-ma))