n=int(input())
r=1
for i in range(n):
    r=(r*2)%1000000007
print(r)