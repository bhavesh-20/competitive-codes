def dfs(a,visited,i,n,t):
    visited[i]=1
    for j in range(n):
        if visited[j]==0 and a[i][j]>t:
            dfs(a,visited,j,n,a[i][j])
    

for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    mi=100000000000
    ma=0
    l=[]
    for i in range(n):
        r=[0]*n
        for j in range(n):
            #i + a[i]*t = j + a[j]*t
            if i==j:
                r[i] = 0
            else:
                if i<j:
                    if (a[j]-a[i])!=0:
                        t=(j-i)/(a[i]-a[j])
                        if t>0:
                            r[j]=t
                else:
                    if (a[j]-a[i])!=0:
                        t=(i-j)/(a[j]-a[i])
                        if t>0:
                            r[j]=t
        l.append(r[:])
    #print(l)
    for i in range(n):
        visited=[0]*n
        dfs(l,visited,i,n,0)
        ones=0
        for i in visited:
            if i==1:
                ones+=1
        mi=min(ones,mi)
        ma=max(ones,ma)
    print(mi,ma)