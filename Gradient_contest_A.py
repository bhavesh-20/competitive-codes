#https://codeforces.com/gym/294377/problem/A
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    for i in l:
        print(i,end=' ')
    print("")