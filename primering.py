#https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=465
#prime ring problem uVA online judge
#python version.
#there might be a input problem resulting in tle which i am not sure but this is the same code written in python 
#refer primering.cpp
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
l=[]

def solve(n,i,v):
    v[i]=1
    l.append(i+1)
    for j in range(n):
       if isPrime(l[-1]+j+1) and v[j]==0:
            solve(n,j,v)
    if len(l)==n and isPrime(l[0]+l[-1]):
        for k in range(len(l)-1):
            print(l[k],end=' ')
        print(l[-1])
    if j==n-1:
        v[i]=0
        l.pop()

t=0
while True:
    n=input()
    if n=='':
        break;
    else:
        if t>=1:
            print("")
        t+=1
        n=int(n)
        v=[0]*n
        print("Case {}:".format(t))
        if n%2==0: 
            solve(n,0,v)