# class Solution:
#     def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
#         def helper(n):
#             cnt=res=0
#             for x in nums:
#                 if x<=n:
#                     cnt+=1
#                     res+=cnt
#                 else: cnt=0
#             return res
        
#         return helper(right)-helper(left-1)


# class Solution:
#     def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:
        
#         n=len(nums)
#         start,dp=0,[0]*n
#         for i,x in enumerate(nums):
#             if l<=x<=r:
#                 dp[i]=i-start+1
#             elif x<l:
#                 dp[i]=dp[i-1]
#             elif r<x:
#                 dp[i]=0
#                 start=i+1
#         return sum(dp)

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:
        
        res=start=state=0
        for i,x in enumerate(nums):
            if l<=x<=r:
                state=i-start+1
                res+=state
            elif x<l:
                res+=state
            elif r<x:
                state=0
                start=i+1
        return res
                

