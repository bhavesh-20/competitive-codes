#https://codeforces.com/contest/701/problem/C
n=int(input())
s=input()
se=set()
d=dict()
k=0
for i in s:
    if i not in se:
        se.add(i)
        k+=1
        d[i]=0
queue=[]
mi=100000000000
cnt=0
for i in range(n):
    if d[s[i]]==0:
        cnt+=1
    d[s[i]]+=1
    queue.append(i)
    while cnt==k:
        temp=i-queue[0]+1
        mi=min(mi,temp)
        x=queue.pop(0)
        d[s[x]]-=1
        if d[s[x]]==0:
            cnt-=1
print(mi)
