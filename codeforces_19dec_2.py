n=int(input())
if n==1:
    print(4)
else:
    if n%2==0:
        l=n//2
        r=n//2
        ans=(l+1)*(r+1)
    else:
        l=n//2
        r=n//2
        ans=(l+2)*(r+1)+(r+2)*(l+1)
    print(ans)