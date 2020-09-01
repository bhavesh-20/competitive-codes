n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n-1):
    a.append(abs(l[i]-l[i+1]))

m=-10000000000

for i in range(len(a)):
    sum=0
    z=0
    for j in range(i,len(a)):
        if z==0:
            sum+=a[j]
            z=1
        else:
            sum-=a[j]
            z=0
        m=max(m,sum)
print(m)