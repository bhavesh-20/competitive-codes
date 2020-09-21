#https://codeforces.com/gym/294377/problem/I
def recursive(cost,hunger,b,i,c,visited,m,h):
    c+=cost[i]
    h+=hunger[i]
    visited[i]=1
    visited[i+1]=1
    for j in range(len(cost)):
        if visited[j]==0 and visited[j+1]==0 and c+cost[j]<=b:
            recursive(cost,hunger,b,j,c,visited,m,h);
    m[0]=max(m[0],h)
    visited[i]=0
    visited[i+1]=0
    c-=cost[i]
    h-=hunger[i]

for _ in range(int(input())):
    n,b=map(int,input().split())
    c=[int(x) for x in input().split()]
    h=[int(x) for x in input().split()]
    cost=[]
    hunger=[]
    m=[0]
    for i in range(n-1):
        cost.append(c[i]+c[i+1])
        hunger.append(h[i]+h[i+1])
    for i in range(len(cost)):
        visited=[0]*n
        recursive(cost,hunger,b,i,0,visited,m,0)
    print(m[0])
