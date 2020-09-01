def couting_sort(a):
    n=len(a)
    m=max(a)
    count=[0]*(m+1)
    for i in a:
        count[i]+=1
    for i in range(1,m+1):
        count[i]+=count[i-1]    
    b=a[:]
    count.pop()
    count.insert(0,0)
    for i in range(n):
        ind=count[a[i]]
        b[ind]=a[i]
        count[a[i]]+=1
    return b

n=int(input())
while n!=0:
    l=[int(x) for x in input().split()]
    l=couting_sort(l)
    for i in range(n-1):
        print(l[i],end=' ')
    print(l[n-1])
    n=int(input())