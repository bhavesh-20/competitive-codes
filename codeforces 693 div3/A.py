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

def solve(w,h,n):
	cnt1=cnt2=0
	while w%2==0:
		w//=2
		cnt1+=1
	while h%2==0:
		h//=2
		cnt2+=1
	if cnt1==0 and cnt2==0:
		if n==1:
			print("YES")
		else:
			print("NO")
	else:
		ans=2**(cnt1+cnt2)
		if ans>=n:
			print("YES")
		else:
			print("NO")

def main():
	for _ in range(inp()):
		w,h,n=stdmul()
		solve(w,h,n)
	pass


if __name__ == '__main__':
    main()