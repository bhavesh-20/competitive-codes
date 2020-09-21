#https://codeforces.com/gym/294377/problem/H
n=int(input())
if n==0:
    print(0)
elif n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(3)
else:
    cnt=n//3
    rem=n%3
    if rem!=0:
        if rem==1:
            new=3+rem
            ans=3**(cnt-1)*new
        elif rem==2:
            ans=3**(cnt)*2
    else:
        ans=3**(cnt)
    print(ans)

