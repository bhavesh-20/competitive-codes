def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=a[:]
    b.sort()
    c=[]
    for i in range(n):
        if a[i]!=b[i]:
            c.append(a[i])
    if len(c)==0:
        print("YES")
    else:
        g=b[0]
        for i in range(0,len(c)):
            g=gcd(g,c[i])
        if g==b[0]:
            print("YES")
        else:
            print("NO")