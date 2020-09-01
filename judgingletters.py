for _ in range(int(input())):
    n=int(input())
    d=dict()
    for i in range(n):
        s=input()
        for i in s:
            try:
                d[i]+=1
            except:
                d[i]=1
    z=0
    for i in d:
        if d[i]%n!=0:
            z=1
            break
    if z==1:
        print("NO")
    else:
        print("YES")