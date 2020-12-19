import math
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[]
    for i in range(n):
        x=int(math.log2(a[i]))
        x=1<<x
        b.append(x)
    for i in b:
        print(i,end=' ')
    print(" ")