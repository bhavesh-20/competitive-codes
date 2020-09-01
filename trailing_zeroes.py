n=int(input())
x=5
cnt=0
while n//x!=0:
    cnt+=(n//x)
    x*=5
print(cnt)