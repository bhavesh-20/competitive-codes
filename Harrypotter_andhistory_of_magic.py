#https://codeforces.com/contest/65/problem/B
n=int(input())
a=[]
for _ in range(n):
    a.append(input())

prev="1000"
z=1
for i in range(n):
    l=''
    for j in range(4):
        x=list(a[i][:]) 
        for k in range(10):
            x[j]=chr(k+ord('0'))
            check=''.join(r for r in x)
            if int(check)>=int(prev):
                if len(l)==0:
                    l=check
                else:
                    if int(check)<int(l):
                        l=check

    a[i]=''.join(r for r in l)
    if int(a[i])>2011 or int(a[i])<int(prev):
        z=0
        break;
    prev=a[i]
if z==1:
    for i in a:
        print(i)
    #print(a)
else:
    #print(a)
    print("No solution")