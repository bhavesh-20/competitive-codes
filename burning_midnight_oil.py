#https://codeforces.com/contest/165/problem/B
def f(v,k):
    s=0
    while v!=0:
        s+=v
        v//=k
    return s

def bs(n,k):
    low=0
    high=n-1
    while low<=high:
        mid=low+high
        mid//=2
        ans=f(mid,k)
        #print(ans,mid,x,low,high)
        if ans<n:
            low=mid+1
        elif ans>n:
            high=mid-1
        else:
            return mid
    return low

n,k=map(int,input().split())
print(bs(n,k))