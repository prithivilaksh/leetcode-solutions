class Solution:
    def possibleToStamp(self, grid: List[List[int]], h: int, w: int) -> bool:
        
        def area(dp,r1,c1,r2,c2):
            return dp[r2+1][c2+1]-dp[r1-1+1][c2+1]-dp[r2+1][c1-1+1]+dp[r1-1+1][c1-1+1]
        
        m,n=len(grid),len(grid[0])
        def precompute(mat):
            dp=[[0]*(n+1) for _ in range(m+1)]
            for i in range(m):
                for j in range(n):
                    dp[i+1][j+1]=dp[i-1+1][j+1]+dp[i+1][j-1+1]-dp[i-1+1][j-1+1]+mat[i][j]
            return dp

        psum=precompute(grid)
        grid2=[[0]*n for i in range(m)]
        for i in range(m-h+1):
            for j in range(n-w+1):
                if area(psum,i,j,i+h-1,j+w-1)==0: grid2[i][j]=1
        
        psum2=precompute(grid2)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and area(psum2,max(0,i-h+1),max(0,j-w+1),i,j)==0: return False
        return True

# class Solution:
#     def possibleToStamp(self, grid, H, W):
#         def acc_2d(grid):
#             dp = [[0] * (n+1) for _ in range(m+1)] 
#             for c, r in product(range(n), range(m)):
#                 dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] - dp[r][c] + grid[r][c]
#             return dp

#         def sumRegion(r1, c1, r2, c2):
#             return dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]  

#         m, n = len(grid), len(grid[0])
#         dp = acc_2d(grid)

#         diff = [[0] * (n+1) for _ in range(m+1)] 
#         for c in range(n - W + 1):
#             for r in range(m - H + 1):
#                 if sumRegion(r, c, r + H - 1, c + W - 1) == 0:
#                     diff[r][c] += 1
#                     diff[r][c+W] -= 1
#                     diff[r+H][c] -= 1
#                     diff[r+H][c+W] += 1
        
#         dp2 = acc_2d(diff)
#         for c, r in product(range(n), range(m)):
#             if dp2[r+1][c+1] == 0 and grid[r][c] != 1: return False

#         return True