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

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007

f=[1,2,6,24,120,720,5040,40320,362880,3628800]

def fact(x):
    global f
    return f[x-1]

def main():
    s1=strng()
    s2=strng()
    s1_plus=s1_minus=0
    s2_plus=s2_minus=0
    q=0
    for i in range(len(s1)):
        if s1[i]=='+':
            s1_plus+=1
        else:
            s1_minus+=1
        if s2[i]=='+':
            s2_plus+=1
        elif s2[i]=='-':
            s2_minus+=1
        else:
            q+=1
    x=s1_plus-s2_plus
    y=s1_minus-s2_minus
    if x<0 or y<0:
        ans=0
    elif x==0 or y==0:
        ans=1/(2**q)
    else:
        num=fact(q)/(fact(x)*fact(y))
        den=2**q
        ans=num/den
        pass
    print("%.11f"%ans)
main()