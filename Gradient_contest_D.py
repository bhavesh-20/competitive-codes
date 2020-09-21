#https://codeforces.com/gym/294377/problem/D
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    s=0
    tot_sum=sum(a)
    m=10000000000000000000000
    for i in range(n):
        s+=a[i]
        tot_sum-=a[i]
        diff=abs(s-tot_sum)
        m=min(m,diff)
    print(m)