import sys

sys.setrecursionlimit(100000)
def dfs(d,i,visited,c,initial,m):
    visited[i]=True
    if i==0:
        m[0]+=1
        initial[i]=c[i]
    for j in d[i]:
        if visited[j]==False:
            if initial[i]!=c[j]:
                initial[j]=c[j]
                m[0]+=1
            else:
                initial[j]=initial[i]
            dfs(d,j,visited,c,initial,m)
n=int(input())
a=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
initial=[-1 for i in range(n)]
d=dict()

for i in range(n):
    d[i]=set()

for i in range(n-1):
    d[i+1].add(a[i]-1)
    d[a[i]-1].add(i+1)


visited=[False for i in range(n)]
m=[0]
dfs(d,0,visited,c,initial,m)
print(m[0])