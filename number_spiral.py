inp=lambda a: map(int,a)
inp_list=lambda a: [int(x) for x in a]

for _ in range(int(input())):
    x,y=inp_list(input().split())
    if x>y:
        m=x
        if m%2==0:
            a=m*m
            a=a-(y-1)
        else:
            a=(m-1)*(m-1) + 1
            a=a+(y-1)
    else:
        m=y
        if m%2==0:
            a=(m-1)*(m-1)+1
            a=a+(x-1)
        else:
            a=m*m
            a=a-(x-1)
    print(a)
