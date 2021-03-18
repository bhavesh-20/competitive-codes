#https://codeforces.com/contest/1497/problem/C1
#https://codeforces.com/contest/1497/problem/C2
for _ in range(int(input())):
    n,k = map(int,input().split())
    for i in range(k-3):
        n-=1
        print(1,end=' ')
    if n%3==0:
        print(n//3,n//3,n//3)
    else:
        if n%2==0:
            if n%4==0:
                print(n//2,(n//2)//2,(n//2)//2)
            else:
                print(2,n//2 - (n//2)%2,n - (n//2 - (n//2)%2 + 2))
        else:
            print(1,n//2,n//2)
