#http://codeforces.com/problemset/problem/637/B
stack=[]
s=set()
l=[]
for _ in range(int(input())):
    stack.append(input())
while len(stack)!=0:
    x=stack.pop()
    if x not in s:
        s.add(x)
        l.append(x)
for i in l:
    print(i)