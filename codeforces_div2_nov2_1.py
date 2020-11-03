#https://codeforces.com/contest/1443/problem/A

def myfun(n):
    i=1
    cnt=0
    while i<n:
        i*=2;
        cnt+=1
    return cnt+1
for _ in range(int(input())):
    n=int(input())
    i=0
    for j in range(n):
        print(4*n-i,end=" ")
        i+=2
    print("")
    