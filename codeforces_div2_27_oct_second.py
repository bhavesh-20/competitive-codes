#https://codeforces.com/contest/1437/problem/B
for _ in range(int(input())):
    n=int(input())
    s=input()
    one_count=0
    zero_count=0
    ans=0
    ans2=0
    for i in s:
        if i=='1':
            one_count+=1
            if zero_count>0:
                ans2+=(zero_count-1)
                zero_count=0
        else:
            zero_count+=1
            if one_count>0:
                ans+=(one_count-1)
                one_count=0
    if one_count>0:
        ans+=(one_count-1)
    if zero_count>0:
        ans2+=(zero_count-1)
    print(max(ans,ans2))