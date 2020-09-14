import math
for _ in range(int(input())):
    x,y,k=map(int,input().split())
    number_of_sticks=k+k*y
    n=(number_of_sticks-1)//(x-1)
    if 1+n*(x-1)<number_of_sticks:
        ans=n+1+k
    else:
        ans=n+k
    print(ans)