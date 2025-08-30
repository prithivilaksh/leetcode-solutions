# class Solution:
#     def uniquePaths(self, grid: List[List[int]]) -> int:

#         m,n=len(grid),len(grid[0])
#         mod=10**9+7
        
#         @cache
#         def helper(i,j,pIsLeft):
#             if i<0 or i==m or j<0 or j==n: return 0
#             if i==m-1 and j==n-1: return 1

#             if grid[i][j]:
#                 if pIsLeft: return helper(i+1,j,False)
#                 else: return helper(i,j+1,True)

#             return (helper(i,j+1,True)+helper(i+1,j,False))%mod

#         return helper(0,0,0)


# class Solution:
#     def uniquePaths(self, grid: List[List[int]]) -> int:

#         m,n=len(grid),len(grid[0])
#         mod=10**9+7

#         dp=[[[0]*2 for _1 in range(n+1)] for _2 in range(m+1)]

#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 for d in (0,1): #from left/from top
#                     if i==m-1 and j==n-1: dp[i][j][d]=1
#                     elif grid[i][j]==1:
#                         if d==0: dp[i][j][0]=dp[i+1][j][1]
#                         else: dp[i][j][1]=dp[i][j+1][0]
#                     else:
#                         dp[i][j][d]=(dp[i][j+1][0]+dp[i+1][j][1]) % mod

#         return dp[0][0][0]
                            
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        m,n=len(grid),len(grid[0])
        mod=10**9+7

        dp=[[[0]*2 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1: dp[i][j][0]=dp[i][j][1]=1
                elif grid[i][j]==0: dp[i][j][0]=dp[i][j][1]=(dp[i][j+1][0]+dp[i+1][j][1]) % mod
                else:
                    dp[i][j][0]=dp[i+1][j][1]
                    dp[i][j][1]=dp[i][j+1][0]

        return dp[0][0][0]
        