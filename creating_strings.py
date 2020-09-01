class Solution(object):
   def __init__(self):
      super().__init__()
   def nextPermutation(self, nums):
      found = False
      i = len(nums)-2
      while i >=0:
         if nums[i] < nums[i+1]:
            found =True
            break
         i-=1
      if not found:
         nums.sort()
      else:
         m = self.findMaxIndex(i+1,nums,nums[i])
         nums[i],nums[m] = nums[m],nums[i]
         nums[i+1:] = nums[i+1:][::-1]
      return nums
   def findMaxIndex(self,index,a,curr):
      ans = -1
      index = 0
      for i in range(index,len(a)):
         if a[i]>curr:
            if ans == -1:
               ans = curr
               index = i
            else:
               ans = min(ans,a[i])
               index = i
      return index

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

ob=Solution()      
s=list(input())
d=dict()
for i in s:
    try:
        d[i]+=1
    except:
        d[i]=1
n=fact(len(s))
for i in d:
    n=n//(fact(d[i]))
s.sort()
print(n)
print(''.join(x for x in s))
for i in range(n-1):
    s=ob.nextPermutation(s)
    print(''.join(x for x in s))