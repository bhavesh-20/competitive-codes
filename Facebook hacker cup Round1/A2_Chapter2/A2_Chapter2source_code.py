for _t in range(int(input())):
    n = int(input())
    s = input()
    cnt, mod, prev = 0, 10**9+7, None
    for i in s:
        if i!='F':
            prev=i
            break
    current, new, previous, fs = 0, 0, 0, 0
    for i in s:
        if i!='F':
            if prev!=i:
                current, previous = ( (current * 2)%mod - previous + new)%mod, current
                cnt = (cnt + current)%mod
                new = 1 + fs
                fs =  0
                prev = i
            else:
                new+=fs+1
                fs=0
                cnt = (cnt + current)%mod
        else:
            fs += 1
            cnt = (cnt + current)%mod
        # print(current, previous, fs, prev_fs)

    ans = f"Case #{_t+1}: {cnt}"
    print(ans)