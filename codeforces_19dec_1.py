for _ in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()
    red=0
    blue=0
    equal=0
    for i in range(n):
        if s1[i]==s2[i]:
            equal+=1
        elif s1[i]>s2[i]:
            red+=1
        else:
            blue+=1
    if red>blue:
        print("RED")
    elif red<blue:
        print("BLUE")
    else:
        print("EQUAL")