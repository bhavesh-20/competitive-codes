import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))
lis    =lambda: list(input().strip().split())

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline().strip()
stdint =lambda: int(stdin.readline())
stdmul =lambda: map(int,stdin.readline().strip().split())
stdseq =lambda: list(map(int,stdin.readline().strip().split()))
stdlis =lambda: list(stdin.readline().strip().split())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007

#Complexity: O(max(log2(a), log2(b)))
def gcd(a,b):
	while b:
		a,b=b,a%b
	return a

#Complexity: O(max(log2(a), log2(b)))
def lcm(a,b):
	w=a//gcd(a,b)
	return w*b

#returns a^b
#Complexity: O(log2(b))
def expo(a,b):
	x,y=1,a
	while(b>0):
		if(b&1):
			x=x*y
		y=y*y
		b>>=1
	return x

#return (a ^ b) mod m
#Complexity: O(log2(b))
def power(a,b,m):
	x,y=1,
	while(b>0):
		if(b&1):
			x=mod(x,y,m)
		y=mod(y,y,m)
		b>>=1
	return x

#returns (a ^ (-1)) mod m
#works only for m = prime
#Complexity: O(log2(m))
def inv(a,m):
	return power(a,m-2,m)

def mod_inverse(a, n):
	N = n
	xx = 0
	yy = 1
	y = 0
	x = 1
	while(n > 0):
		q = a // n
		t = n
		n = a % n
		a = t
		t = xx
		xx = x - q * xx
		x = t
		t = yy
		yy = y - q * yy
		y = t
	x %= N
	x += N
	x %= N
	return x

#pass an array into sieve to get primes into it instead of doing it globally
#primes=[0]*1000000

#Complexity: O(n * log2(log2(n)))
def sieve(primes):
	primes[1]=1
	primes[2]=2
	j=4
	while(j<1000000):
		primes[j]=2
		j+=2
	j=3
	while(j<1000000):
		if primes[j]==0:
			primes[j]=j
			i=j*j
			k=j<<1
			while(i<1000000):
				primes[i]=j
				i+=k
		j+=2

def main():
	n=stdint()
	a=stdseq()
	a.sort()
	m=a[-1]-a[0]
	cnt=0
	x=a[-1]
	c=a[0]
	cnt2=0
	for i in range(n):
		if a[i]==x:
			cnt+=1
		if a[i]==c:
			cnt2+=1
	if x!=c:
		print(m,cnt*cnt2)
	else:
		print(m,cnt*(cnt-1)//2)
	


if __name__ == '__main__':
    main()