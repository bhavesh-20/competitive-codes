for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    s = sum(a)
    print(a[-1] + (s-a[-1])/(n-1))