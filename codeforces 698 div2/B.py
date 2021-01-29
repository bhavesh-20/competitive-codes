def custome_func(a,d):
    if a<0:
        return False
    while a!=0:
        if a%10==d:
            return True
        a//=10
    return False



for _ in range(int(input())):
    q,d=map(int,input().split())
    a=[int(x) for x in input().split()]
    arr = [d*i for i in range(0,10)]
    for i in range(q):
        flag=False
        if a[i]>=d*10:
            print("Yes")
            continue
        for j in range(len(arr)):
            if custome_func(a[i]-arr[j],d):
                print("Yes")
                flag=True
                break
        if flag==False:
            print("No")
