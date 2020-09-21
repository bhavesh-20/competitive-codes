#https://codeforces.com/gym/294377/problem/E
for _ in range(int(input())):
    n=int(input())
    entry=[]
    out=[]
    for i in range(n):
        x,y=map(int,input().split())
        entry.append(x)
        out.append(y)
    queries=[0]*(max(out)+1)
    for i in range(n):
        x=entry[i]
        y=out[i]
        queries[x-1]+=1
        queries[y-1]-=1
    for i in range(1,len(queries)):
        queries[i]+=queries[i-1]
    for q in range(int(input())):
        r=int(input())
        print(queries[r-1])