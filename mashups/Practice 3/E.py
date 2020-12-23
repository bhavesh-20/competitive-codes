k,p=map(int,input().split())
s='1'
ans=0
for i in range(k):
    r=s+s[::-1]
    ans+=(int(r))
    s=str(int(s)+1)
print(ans%p)