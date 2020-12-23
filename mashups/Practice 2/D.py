def dfs(d,i,visited,cnt,m):
    visited[i]=True
    cnt+=1
    m[0]=max(m[0],cnt)
    for j in d[i]:
        if visited[j]==False:
            dfs(d,j,visited,cnt,m)

n=int(input())
d=dict()
visited=dict()
for i in range(n):
    s=input().split()
    s[0]=s[0].lower()
    s[2]=s[2].lower()
    if s[2] in d:
        d[s[2]].append(s[0])
    else:
        d[s[2]]=[s[0]]
    if s[0] not in d:
        d[s[0]]=[]
    visited[s[2]]=False
    visited[s[0]]=False

m=[0]
dfs(d,"polycarp",visited,0,m)
print(m[0])