#https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=2531
c=[0]*100000
for t in range(int(input())):
#for t in range(1):
    n,m,k=map(int,input().split())
    #n,m,k=20,12,4
    a=[1,2,3]
    cnt=0
    mi=1000000000000
    queue=[]
    for i in range(3,n):
        sum=a[i-1]+a[i-2]+a[i-3]
        sum%=m
        a.append(sum+1)
    for i in range(n):
        if a[i]>=1 and a[i]<=k:
            if c[a[i]-1]==0:
                cnt+=1
            c[a[i]-1]+=1
            queue.append(i)
        while cnt==k:
            temp=i-queue[0]+1
            mi=min(mi,temp)
            c[a[queue[0]]-1]-=1
            if c[a[queue[0]]-1]==0:
                cnt-=1
            queue.pop(0)
    print(a)
    if mi==1000000000000:
        print("Case #{}: {}".format(t+1,"sequence nai"))
    else:
        print("Case #{}: {}".format(t+1,mi))