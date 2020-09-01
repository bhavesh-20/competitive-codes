n=int(input())
l=[n]
while n!=1:
    if n%2==0:
        n//=2
    else:
        n=n*3+1
    l.append(n)
for i in l:
    print(i,end=' ')
