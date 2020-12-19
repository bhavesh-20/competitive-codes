for _ in range(int(input())):
    l=list(map(int,input().split()))
    s=sum(l)
    if s%9==0:
        if min(l)>=s//9:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

    



    