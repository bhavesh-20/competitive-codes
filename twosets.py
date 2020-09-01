n=int(input())
l=[x for x in range(1,n+1)]
ans1=[]
ans2=[]
z=1
if n%4==0:
    print("YES")
    for i in range(n//2):
        if z==1:
            z=0
            ans1.append(l[i])
            ans1.append(l[n-i-1])
        else:
            z=1
            ans2.append(l[i])
            ans2.append(l[n-i-1])
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
    a=l[3:]
    m=len(a)
    for i in range(len(a)//2):
        if z==1:
            z=0
            ans1.append(a[i])
            ans1.append(a[m-i-1])
        else:
            z=1
            ans2.append(a[i])
            ans2.append(a[m-i-1])
    print(len(ans1))
    for i in ans1:
        print(i,end=' ')
    print('')
    print(len(ans2))
    for i in ans2:
        print(i,end=' ')
else:
    print("NO")