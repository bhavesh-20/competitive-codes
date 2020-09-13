#https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9
for _t in range(int(input())):
    n=int(input())
    a=[]
    l=[]
    for i in range(n):
        x,y=input().split()
        x,y=int(x),int(y)
        a.append([x,y])
        l.append([x,y])    
    a.sort()
    j=c=1;
    jfri=cfri=jfrf=cfrf=0
    flag=0;
    r=[]
    for i in range(n):
        if j==1:
            j=0;
            jfri=a[i][0]
            jfrf=a[i][1]
            r.append('J');
        else:
            if jfrf<=a[i][0]:
                jfrf=a[i][1]
                jfri=a[i][0]
                r.append('J')
            else:
                if c==1:
                    c=0;
                    cfrf=a[i][1]
                    cfri=a[i][0]
                    r.append('C')
                else:
                    if cfrf<=a[i][0]:
                        cfrf=a[i][1]
                        cfri=a[i][0]
                        r.append('C')
                    else:
                        flag=1;
                        break;
    if flag==0:
        q=[]
        for i in range(n):
            ind=a.index(l[i])
            a[ind]=[-1,-1]
            q.append(r[ind])
        string=''.join(x for x in q)
    else:
        string="IMPOSSIBLE"
    print("Case #{}: {}".format(_t+1,string))
    