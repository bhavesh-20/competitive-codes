#https://codeforces.com/contest/1409/problem/D
def sum(n):
  d =  0
  for i in list(str(n)):
    d += int(i)
  return d


for i in range(int(input())):
    n, s = map(int, input().split())
    ans = []
    while sum(n) > s:
        ans.insert(0, str((10 - n%10)%10))
        n=n//10 + (1 if n%10 else 0)
    if len(ans) == 0:
        print(0)
        continue;
    print(''.join(ans))