#https://codeforces.com/contest/1406/problem/B
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    pos=[]
    neg=[]
    for i in a:
        if i>=0:
            pos.append(i)
        else:
            neg.append(i)
    pos.sort(reverse=True)
    neg.sort()
    x=pos[:5]
    y=neg[:5]
    l=x+y
    m=len(l)
    max=-100000000000000000000000000000000000
    for i in range(m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                for o in range(k+1,m):
                    for p in range(o+1,m):
                        ans=l[i]*l[j]*l[k]*l[o]*l[p]
                        if ans>max:
                            max=ans
    if max<0:
        m1=len(pos)
        m2=len(neg)
        if m1==0:
            ans=neg[-1]*neg[-5]*neg[-2]*neg[-3]*neg[-4]
        elif m1==2:
            ans=pos[-1]*pos[-2]*neg[-1]*neg[-2]*neg[-3]
        elif m1==4:
            ans=pos[-1]*pos[-2]*pos[-3]*pos[-4]*neg[-1]
        print(ans)
    else:
        print(max)