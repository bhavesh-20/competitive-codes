x,y=list(map(int,input().split()))
cnt=0
while True:
    if cnt%2==0:
        if x>=2 and y>=2:
            num_100=2
        elif y>=22:
            num_100=0
        elif x>=1 and y>=12:
            num_100=1
        else:
            break
        num_10=(220-100*num_100)//10
        x-=num_100
        y-=num_10
    else:
        if y>=22:
            num_10=22
        elif y>=12 and x>=1:
            num_10=12
        elif y>=2 and x>=2:
            num_10=2
        else:
            break
        num_100=(220-10*num_10)//100
        x-=num_100
        y-=num_10
    cnt+=1
if cnt%2==0:
    print("Hanako")
else:
    print("Ciel")