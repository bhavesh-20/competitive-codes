for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append([int(x) for x in input().split()])
    cnt=0
    z=0
    for i in range(0,n):
        if a[0][i]==i+1:
            z=i
        else:
            if i+1<n and a[0][i+1]!=i+2:
                continue
            else:
                if z==0:
                    z=i
                    cnt+=1
                else:
                    cnt+=2
    print(cnt)