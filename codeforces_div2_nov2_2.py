#https://codeforces.com/contest/1443/problem/B
for _ in range(int(input())):
    a,b=map(int,input().split())
    s=input()
    note=1
    if note==0:
        cnt=0
        for i in s:
            if i=='1':
                cnt+=1
        print(cnt*a)
    else:
        n=len(s)
        ans=0
        cnt=0
        trigger=0
        for i in range(n):
            if s[i]=='1':
                if trigger==0:
                    ans+=a
                    trigger=1
                else:
                    if cnt*b>a:
                        ans+=a
                    else:
                        ans+=(cnt*b)
                cnt=0
            else:
                cnt+=1
        print(ans)