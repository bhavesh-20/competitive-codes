inp=lambda a: map(int,a)
inp_list=lambda a: [int(x) for x in a]

def f():
    print("YES")

a=[]
l=[0,1,2,3]
for _ in range(4):
    a.append(inp_list(input().split()))
for i in range(4):
    z=0
    for j in range(3):
        if a[i][j]==1:
            if j==0:
                if a[(i+3)%4][3]==1 or a[i][3]==1:
                    f()
                    z=1
                    break
            elif j==1:
                if a[(i+2)%4][3]==1 or a[i][3]==1:
                    f()
                    z=1
                    break
            elif j==2:
                if a[(i+1)%4][3]==1 or a[i][3]==1:
                    f()
                    z=1
                    break
    if z==1:
        break
if z==0:
    print("NO")
