for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    d=dict()
    m=0
    for i in a:
        try:
            d[i]+=1
        except:
            d[i]=1
        m=max(d[i],m)
    print(m)