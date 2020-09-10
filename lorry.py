#https://codeforces.com/problemset/problem/3/B
n,c=map(int,input().split())

ones=[]
twos=[]
cnt=0
for i in range(n):
    cnt+=1
    x,y=map(int,input().split())
    if x==1:
        ones.append([y,cnt])
    else:
        twos.append([y,cnt])

ones.sort(key=lambda s:-s[0])
twos.sort(key=lambda s:-s[0])

sum=0
pt_1=0
pt_2=0

ans=[]

m1=len(ones)
m2=len(twos)

while c>0:
    if pt_1<m1:
        if pt_2<m2:
            if pt_1+1<m1:
                if ones[pt_1][0]+ones[pt_1+1][0]<=twos[pt_2][0] and c>=2:
                    sum+=(twos[pt_2][0])
                    c-=2
                    ans.append(twos[pt_2][1])
                    pt_2+=1
                else:
                    sum+=(ones[pt_1][0])
                    c-=1
                    ans.append(ones[pt_1][1])
                    pt_1+=1
            else:
                if ones[pt_1][0]<twos[pt_2][0] and c>=2:
                    sum+=(twos[pt_2][0])
                    c-=2
                    ans.append(twos[pt_2][1])
                    pt_2+=1
                else:
                    sum+=(ones[pt_1][0])
                    c-=1
                    ans.append(ones[pt_1][1])
                    pt_1+=1
        else:
            c-=1
            ans.append(ones[pt_1][1])
            sum+=ones[pt_1][0]
            pt_1+=1
    else:
        if c>=2:
            if pt_2<m2:
                c-=2
                sum+=(twos[pt_2][0])
                ans.append(twos[pt_2][1])
                pt_2+=1
            else:
                break
        else:
            break;
print(sum)
for i in ans:
    print(i,end=' ')