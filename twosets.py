n=int(input())
ans1=[]
ans2=[]
z=1
if n%4==0:
    print("YES")
    for i in range(1,n//2+1):
        if z==1:
            z=0
            ans1.append(i)
            ans1.append(n-i+1)
        else:
            z=1
            ans2.append(i)
            ans2.append(n-i+1)
    print(len(ans1))
    for i in ans1:
        print(i,end=' ')
    print('')
    print(len(ans2))
    for i in ans2:
        print(i,end=' ')
elif n%4==3:
    print("YES")
    ans1.append(1)
    ans1.append(2)
    ans2.append(3)
    for i in range(4,4+(n-4)//2+1):
        if z==1:
            z=0
            ans1.append(i)
            ans1.append(n-i+4)
        else:
            z=1
            ans2.append(i)
            ans2.append(n-i+4)
    print(len(ans1))
    for i in ans1:
        print(i,end=' ')
    print('')
    print(len(ans2))
    for i in ans2:
        print(i,end=' ')
else:
    print("NO")