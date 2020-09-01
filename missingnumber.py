n=int(input())
l=list(map(int,input().split()))
l.sort()
i=0
while i<n-1:
    if l[i]!=(i+1):
        print(i+1)
        break
    i+=1    
if i==n-1:
    print(i+1)