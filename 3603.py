# class Solution:
#     def minCost(self, m: int, n: int, wc: List[List[int]]) -> int:

#         dp=[[0]*n for i in range(m)]
#         wc[0][0]=0
#         for i in range(m):
#             for j in range(n):
#                 if i-1>=0 and j-1>=0: dp[i][j]=min(dp[i][j-1],dp[i-1][j])
#                 elif j-1>=0: dp[i][j]=dp[i][j-1]
#                 elif i-1>=0: dp[i][j]=dp[i-1][j]
#                 dp[i][j]+=(i+1)*(j+1)+wc[i][j]
                    
#         return dp[m-1][n-1]-wc[m-1][n-1]

class Solution:
    def minCost(self, m: int, n: int, dp: List[List[int]]) -> int:

        dp[0][0]=dp[-1][-1]=0
        for i in range(m):
            for j in range(n): 
                pre = 0 if i==0 and j==0 else inf
                if i: pre=min(pre,dp[i-1][j])
                if j: pre=min(pre,dp[i][j-1])
                dp[i][j]+=(i+1)*(j+1)+pre
                    
        return dp[m-1][n-1]