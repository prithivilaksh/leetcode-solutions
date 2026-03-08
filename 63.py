# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
#         m,n=len(grid),len(grid[0])
#         @cache
#         def dp(i,j):
#             if i==m or j==n or grid[i][j]==1: return 0
#             if i==m-1 and j==n-1: return 1
#             return dp(i+1,j)+dp(i,j+1)
#         return dp(0,0)


# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
#         m,n=len(grid),len(grid[0])
#         if grid[m-1][n-1]: return 0
#         dp=[[0]*(n+1) for i in range(m+1)]
#         dp[m-1][n-1]=1

#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if grid[i][j]!=1:
#                     dp[i][j]+=dp[i+1][j]+dp[i][j+1]
#         return dp[0][0]

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        m,n=len(grid),len(grid[0])
        if grid[m-1][n-1]: return 0
        dp=[0]*(n+1)
        dp[n-1]=1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j]!=1: dp[j]+=dp[j+1]
                else: dp[j]=0
        return dp[0]
