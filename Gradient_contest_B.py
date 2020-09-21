#https://codeforces.com/gym/294377/problem/B
for _ in range(int(input())):
    n,y=map(int,input().split())
    a=[int(x) for x in input().split()]
    cnt=0
    for i in range(n):
        if a[i]==y:
            if i+y-1<n and a[i+y-1]==1:
                cnt+=1
    print(cnt)