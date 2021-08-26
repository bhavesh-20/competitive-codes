for _ in range(int(input())):
    n, k = map(int,input().split())
    a = [int(x) for x in input().split()]
    sorted_a = sorted(a)
    d_next = {}
    for i in range(n-1):
        d_next[sorted_a[i]] = sorted_a[i+1]
    d_next[sorted_a[-1]] = None
    c = 0
    for i in range(n-1):
        if d_next[a[i]] != a[i+1]:
            c+=1
    c+=1
    if k>=c:
        print("Yes")
    else:
        print("No")