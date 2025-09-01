class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(i,j):
            q,res,grid[i][j]=[(i,j)],0,0
            while q:
                i,j=q.pop()
                res+=1
                for i,j in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                    if 0<=i<m and 0<=j<n and grid[i][j]==1:
                        grid[i][j]=0
                        q.append((i,j))
            return res
        
        m,n,res=len(grid),len(grid[0]),0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res=max(res,bfs(i,j))
        return res