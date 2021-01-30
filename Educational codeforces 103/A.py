import math as m
for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%k==0:
        print(1)
        continue
    if n>k:
        new_n = (n//k + 1)*k
        print(1+m.ceil((new_n-n)/n))
    else:
        print(1+m.ceil((k-n)/n))