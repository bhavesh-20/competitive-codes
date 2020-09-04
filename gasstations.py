#https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3743
while True:
    l,g=map(int,input().split())
    if l==0:
        break;
    a=[]
    for _ in range(g):
        x,y=map(int,input().split())
        a.append([max(0,x-y),min(l,x+y)])
    ans=g;
    a.sort()
    start=0
    temp=0
    i=0
    while start<l:
        temp=start
        while i<g and start>=a[i][0]:
            temp=max(a[i][1],temp)
            i+=1
        if start==temp:
            break
        else:
            start=temp
        ans-=1
    print(ans) if start>=l else print(-1)
