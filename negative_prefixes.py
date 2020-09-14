for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]

    l=[]

    for i in range(n):
        if b[i]==0:
            l.append(a[i])

    l.sort(reverse=True)
    j=0
    for i in range(n):
        if b[i]==0:
            a[i]=l[j]
            j+=1

    for i in a:
        print(i,end=' ')
    print('')
