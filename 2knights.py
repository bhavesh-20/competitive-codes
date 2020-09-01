l=[0]+[(i*i)*(i*i-1)//2-(4*(i-2)*(i-1)) for i in range(2,10001)]
for i in range(int(input())):
    print(l[i])