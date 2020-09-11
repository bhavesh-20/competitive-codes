#https://www.codechef.com/COLE2020/problems/CLPNT
def bs(a,n):
    l=0;
    r=len(a)-1
    while l<=r:
        mid=(l+r)//2;
        if a[mid]>n:
            r=mid-1;
        elif a[mid]<n:
            l=mid+1;
        else:
            return -1;
    return l;

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(int(input())):
        x,y=input().split()
        x,y=int(x),int(y)
        sum=x+y;
        ans=bs(a,sum)
        print(ans)