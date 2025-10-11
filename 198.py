# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n=len(nums)
#         @cache
#         def dp(i):
#             if i>=n: return 0
#             a=nums[i]+dp(i+2)
#             b=dp(i+1)
#             return max(a,b)
        
#         return dp(0)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n=len(nums)
#         dp=[0]*(n+2)
#         for i in range(n-1,-1,-1):
#             dp[i]=max(nums[i]+dp[i+2],dp[i+1])
#         return dp[0]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        currp1=currp2=0
        for i in range(n-1,-1,-1):
            curr=max(nums[i]+currp2,currp1)
            currp2=currp1
            currp1=curr
        return curr