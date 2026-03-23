# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
#         nums.sort(reverse=True)
#         n=len(nums)

#         @cache
#         def dp(pos):
#             ans=[nums[pos]]
#             for i in range(pos+1,n):
#                 if nums[pos]%nums[i]==0:
#                     ians=[nums[pos]]+dp(i)
#                     if len(ians)>len(ans):ans=ians
#             return ans
        
#         res=[]
#         for i in range(n):
#             ires=dp(i)
#             if len(ires)>len(res):res=ires 
#         return res

# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
#         nums.sort(reverse=True)
#         n=len(nums)
#         child=defaultdict(lambda: -1)

#         @cache
#         def dp(pos):
#             res=1
#             for i in range(pos+1,n):
#                 if nums[pos]%nums[i]==0:
#                     next=dp(i)
#                     if res<1+dp(i):
#                         res=1+dp(i)
#                         child[pos]=i
#             return res
        
#         res,start=1,0
#         for i in range(n):
#             ires=dp(i)
#             if ires>res:
#                 res,start=ires,i
#         res=[]
#         while start!=-1:
#             res.append(nums[start])
#             start=child[start]
        
#         return res


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort(reverse=True)
        n=len(nums)
        dp,next=[1]*n,[-1]*n
        start=n-1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]%nums[j]==0 and dp[i]<1+dp[j]:
                    dp[i]=1+dp[j]
                    next[i]=j
            
            if dp[i]>dp[start]:
                start=i
        
        res=[]
        while start!=-1:
            res.append(nums[start])
            start=next[start]
        return res

# class Solution:
#     def largestDivisibleSubset(self, nums):
#         if len(nums) == 0: return []
#         nums.sort()
#         sol = [[num] for num in nums]
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
#                     sol[i] = sol[j] + [nums[i]]
#         return max(sol, key=len)