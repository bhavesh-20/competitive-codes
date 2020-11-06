#https://codeforces.com/gym/302421/problem/B
for _ in range(int(input())):
    n=int(input())
    s=input()
    trigger=0
    ans=''
    onecount=0
    for i in range(n):
        if s[i]=='0':
            if trigger==0:
                ans+='0'
            else:
                trigger=2
        else:
            if trigger==2:
                ans+='x'
                onecount=0
            onecount+=1
            trigger=1
    if trigger==2:
        ans+='x'
        onecount=0
    ans+=('1'*onecount)
    n=len(ans)
    cnt=0
    ans1=''
    for i in range(n):
        if ans[i]=='x':
            cnt+=1
        else:
            if cnt>0:
                cnt=0
                ans1+='0'
            ans1+=ans[i]
    if cnt>0:
        cnt=0
        ans1+='0'
    print(ans1)