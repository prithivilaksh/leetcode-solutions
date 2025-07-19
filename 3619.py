class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        def dfs(i,j):
            res=grid[i][j]
            grid[i][j]=0
            for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                x,y=i+di,j+dj
                if 0<=x<m and 0<=y<n and grid[x][y]!=0:
                    res+=dfs(x,y)
            return res

        m,n,res=len(grid),len(grid[0]),0

        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    res+=(dfs(i,j)%k==0)

        return res