modulo=1000000007
def ncr(n, r, p=1000000007): 
    # initialize numerator 
    # and denominator 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  
            p - 2, p)) % p 

for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    d=dict()
    m=0
    ans=1<<n
    for i in a:
        m=max(m,i)
        try:
            d[i]+=1
        except:
            d[i]=1
    if d[m]%2!=0:
        print(ans%modulo)
    else:
        mi=d[m]
        tech=(1<<(n-mi))%modulo
        print((ans%modulo-(ncr(mi,mi//2)*tech)%modulo)%modulo)