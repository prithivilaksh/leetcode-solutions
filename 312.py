# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
        
#         nums=[1]+nums+[1]
#         n=len(nums)

#         @cache
#         def helper(i,j):
#             res=0
#             for k in range(i,j+1):
#                 left=helper(i,k-1)
#                 mid=nums[i-1]*nums[k]*nums[j+1]
#                 right=helper(k+1,j)
#                 res=max(res,left+mid+right)
#             return res
#         return helper(1,n-2)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-2,0,-1):
            for j in range(i,n-1):
                for k in range(i,j+1):
                    left=dp[i][k-1]
                    mid=nums[i-1]*nums[k]*nums[j+1]
                    right=dp[k+1][j]
                    dp[i][j]=max(dp[i][j],left+mid+right)
        return dp[1][n-2]





        