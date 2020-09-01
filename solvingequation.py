import math 
import random 

def nthRoot(A,N): 
	xPre = random.randint(1,101) % 10
	eps = 0.001
	delX = 2147483647
	xK=0.0
	while (delX > eps): 
		xK = ((N - 1.0) * xPre +
			A/pow(xPre, N-1)) /N 
		delX = abs(xK - xPre) 
		xPre = xK; 
	return xK 

def nroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

n=int(input())
a=[int(x) for x in input().split()]
a.sort()
m=a[n-1]
c=nroot(n-1,m)
k=int(c)+1
c=int(c)
s1=0
s2=0
r1=1
r2=1
for i in range(n):
    s1+=(abs(a[i]-r1))
    s2+=(abs(a[i]-r2))
    r1*=c
    r2*=k
print(min(s1,s2))