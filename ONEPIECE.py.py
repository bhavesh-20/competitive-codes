#https://www.codechef.com/problems/ONEPIECE

import math
for t in range(int(input())):
    n=int(input())
    print((math.factorial(3*n))//(6**n)%1000000007)