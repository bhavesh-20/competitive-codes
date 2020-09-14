for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    f=y=0
    i=1
    if a[0]==1:
        f+=1

    while i<n:
        if a[i]==1:
            if y==0:
                y+=1
            elif y==1:
                y+=1
            else:
                f+=1
                y=0
        else:
            y=0
        i+=1
    print(f)
