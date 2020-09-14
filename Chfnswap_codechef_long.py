import math
for _ in range(int(input())):
    n=int(input())
    if n%4==1 or n%4==2:
        print(0)
    else:
        s=n*(n+1)//2
        #print(n-q)
        check=math.sqrt(1+4*s)
        q=(int(math.sqrt(1+4*s))-1)//2
        cnt=n-q
        if int(check)==check:
            r=n-q
            cnt=cnt+q*(q-1)//2+r*(r-1)//2
        print(cnt)        