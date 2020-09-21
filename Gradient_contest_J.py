#https://codeforces.com/gym/294377/problem/J
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    mul=1
    for i in a:
        mul*=i
    print(pow(k+1,mul,1000000007))