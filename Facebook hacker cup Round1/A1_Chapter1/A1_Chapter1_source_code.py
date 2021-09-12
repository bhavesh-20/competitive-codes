for _t in range(int(input())):
    n = int(input())
    s = input()
    cnt, prev = 0, None
    for i in s:
        if i!='F' and i!=prev:
            prev = i
            cnt+=1
    if cnt!=0:
        cnt-=1
    ans = f"Case #{_t+1}: {cnt}"
    print(ans)