for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    s=set(a)
    s.discard(0);
    print(len(s))