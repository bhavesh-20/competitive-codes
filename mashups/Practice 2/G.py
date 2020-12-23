for _t in range(int(input())):
    n,k=map(int,input().split())
    i=1
    for _ in range(n):
        x=i*(i+1)//2
        if x>=k:
            break
        i+=1
    s=['a' for j in range(n)]
    s[n-1-i]='b'
    i-=1
    x=k-i*(i+1)//2
    s[n-x]='b'
    s=''.join(x for x in s)
    print(s)
