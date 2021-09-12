for _t in range(int(input())):
    n,m,a,b = map(int, input().split())
    x = n+m-1
    if x>a or x>b:
        ans = "Impossible" + "\n"
    else:
        ans = "Possible" + "\n"
        for i in range(n):
            arr = []
            for j in range(m):
                x = n+m-2
                if i==0 and j==0:
                    arr.append(a-x)
                elif i==0 and j==m-1:
                    arr.append(b-x)
                else:
                    arr.append(1)
            ans += ' '.join([str(x) for x in arr]) + "\n"
    ans = f"Case #{_t+1}: {ans}"
    print(ans,end='')