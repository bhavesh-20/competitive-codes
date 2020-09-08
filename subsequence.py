#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3562
while True:
    try:
        s=input()
        n,s=map(int,s.split())
        a=[int(x) for x in input().split()]
        start=0
        sum=0
        mi=10000000000000
        for i in range(n):
            sum+=a[i]
            while sum>=s and start<=i:
                mi=min(mi,i-start+1)
                sum-=a[start]
                start+=1
        if mi==10000000000000:
            mi=0
        print(mi)
    except:
        break