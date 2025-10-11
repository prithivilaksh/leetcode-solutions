# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         n=len(nums)
#         dp=[2]*n
#         dp[0]=1

#         for i in range(2,n):
#             if nums[i-2]+nums[i-1]==nums[i]:
#                 dp[i]=dp[i-1]+1

#         return max(dp)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        ln=res=2
        for i in range(2,n):
            if nums[i-2]+nums[i-1]==nums[i]: ln+=1
            else: ln=2
            res=max(res,ln)

        return res