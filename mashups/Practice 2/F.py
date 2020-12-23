n=input()
s=input()
in_p=0
word_len=0
a=0
b=0
for i in s:
    if i.isalpha():
        word_len+=1
    elif i=='_':
        if in_p==1:
            if word_len>0:
                b+=1
        else:
            a=max(a,word_len)
        word_len=0
    elif i=='(':
        a=max(a,word_len)
        word_len=0
        in_p=1
    elif i==')':
        if word_len>0:
            b+=1
        word_len=0
        in_p=0
a=max(a,word_len)

print(a,b)