#https://codeforces.com/group/fzY0kNJuh2/contest/294236/problem/C
import sys
n=int(input())

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

temp=n
cnt=0
while temp!=0:
    temp//=10
    cnt+=1
if cnt%2!=0:
    print('4'*((cnt+1)//2)+'7'*((cnt+1)//2))
else:
    s=str(n)
    r='7'*(cnt//2)+'4'*(cnt//2)
    if s>r:
        print('4'*((cnt+2)//2)+'7'*((cnt+2)//2))
        sys.exit()
    elif s==r:
        print(s)
        sys.exit()
    r='4'*(cnt//2)+'7'*(cnt//2)
    if s<r:
        print(r)
        sys.exit()
    elif s==r:
        print(s)
        sys.exit()
    for i in a:
        if i>n:
            break
    ss=list(str(i))
    fours=0
    sevens=0
    for i in ss:
        if i=='4':
            fours+=1
        else:
            sevens+=1
    if fours>sevens:
        c=(fours-sevens)//2
        for i in range(len(ss)-1,-1,-1):
            if ss[i]=='4':
                ss[i]='7'
                c-=1
            if c==0:
                break
    else:
        c=(sevens-fours)//2
        for i in range(len(ss)-1,-1,-1):
            if c==0:
                break
            if ss[i]=='7':
                ss[i]='4'
                c-=1
    print(''.join(x for x in ss))