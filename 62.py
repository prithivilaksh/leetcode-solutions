# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         @cache
#         def dp(i,j):
#             if i==m-1 and j==n-1: return 1
#             if i==m or j==n: return 0
#             return dp(i+1,j)+dp(i,j+1)
#         return dp(0,0)

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         dp=[[0]*(n+1) for i in range(m+1)]
#         dp[m-1][n-1]=1

#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 dp[i][j]+=dp[i+1][j]+dp[i][j+1]
#         return dp[0][0]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp=[0]*(n+1)
        dp[n-1]=1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[j]+=dp[j+1]
        return dp[0]

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         dp=[0]*(m+1)
#         dp[m-1]=1

#         for j in range(n-1,-1,-1):
#             for i in range(m-1,-1,-1):
#                     dp[i]+=dp[i+1]
#         return dp[0]