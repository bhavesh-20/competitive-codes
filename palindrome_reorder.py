s=input()
d=dict()
for i in s:
    try:
        d[i]+=1
    except:
        d[i]=1
odd=even=0
for i in d:
    if d[i]%2!=0:
        odd+=1
if odd==0:
    l=[]
    for i in d:
        y=d[i]//2
        l=l+[i]*y
    r=l[:]
    l.reverse()
    r=r+l
    print(''.join(x for x in r))
elif odd==1 and len(s)%2!=0:
    l=[]
    for i in d:
        if d[i]%2==0:
            y=d[i]//2
            l=l+[i]*y
        else:
            y=d[i]//2
            x=i
            l=l+[i]*y
    r=l[:]
    l.reverse()
    r=r+l
    r.insert(len(s)//2,x)
    print(''.join(x for x in r))
else:
    print("NO SOLUTION")
