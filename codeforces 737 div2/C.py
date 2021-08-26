mod = 10**9+7
for _ in range(int(input())):
    n, k = map(int,input().split())
    if k==0:
        print(1)
        continue
    if n%2!=0:
        ans = ((pow(2,n-1,mod)+1)%mod * k)%mod
    else:
        draw = pow(2,n-1,mod) - 1
        x,y = k-1, 0
        ans = 0
        while x>0:
            ans = (ans + (pow(4,x,mod) * pow(draw,y,mod))%mod)%mod
            x-=1
            y+=1
        ans = (ans + pow(draw,k-1,mod)*(draw+1))%mod
    print(ans)
