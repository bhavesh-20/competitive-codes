s=input()
cnt=1
m=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt+=1
    else:
        cnt=1
    m=max(m,cnt)
print(m)