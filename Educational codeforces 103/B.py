import math

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    s = sum(a)
    for i in range(n-1,0,-1):
        s-=a[i]
        number = math.ceil((100*a[i])/k)
        if s<number:
            s=number
    print(s-a[0])   
