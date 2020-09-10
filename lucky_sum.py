#https://codeforces.com/group/fzY0kNJuh2/contest/294236/problem/B
l,r=map(int,input().split())
a=[4,7]
x=1
ri=10**(10)
i=0
while x<ri:
    x=a[i]*10+4
    y=a[i]*10+7
    a.append(x)
    a.append(y)
    i+=1

sum=0
for i in a:
    if l<=i and i<=r:
        sum=sum+(i-l+1)*i
        l=i+1
    if i>r:
        break
print(sum+(r-l+1)*i)