inp=lambda a: map(int,a)
inp_list=lambda a: [int(x) for x in a]

n,k=inp(input().split())
a=inp_list(input().split())
s=set(a)
if len(s)>=k:
    print("YES")
    cnt=0
    for i in range(n):
        if a[i] in s:
            cnt+=1
            s.remove(a[i])
            print(i+1,end=' ')
        if cnt==k:
            break
else:
    print("NO")