#https://codeforces.com/contest/26/problem/B
s=input()
stack=[]
cnt=0
m=0
for i in s:
    if i=='(':
        stack.append(i)
    elif i==')':
        if len(stack)!=0:
            stack.pop()
            cnt+=2
#m=max(m,cnt)
print(cnt)