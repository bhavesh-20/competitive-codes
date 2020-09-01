for _ in range(int(input())):
    x,y=map(int,input().split())
    if (x+y)%3==0:
        if min(x,y)>=(x+y)//3:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")