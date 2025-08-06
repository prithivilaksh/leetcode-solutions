# class Solution:
#     def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        
#         m,n=len(grid),len(grid[0])
#         vis=[[False]*n for i in range(m)]
#         q=deque([])

#         for i in range(m):
#             for j in range(n):
#                 grid[i][j]=grid[i][j]^1
#                 if grid[i][j]==0:
#                     vis[i][j]=True
#                     q.append((i,j))

#         while q:
#             i,j=q.popleft()
#             for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<m and 0<=vj<n and not vis[vi][vj]:
#                         grid[vi][vj]=grid[i][j]+1
#                         vis[vi][vj]=True
#                         q.append((vi,vj))
        
#         return grid


class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        
        m,n,q=len(grid),len(grid[0]),deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]=0
                    q.append((i,j))
                else: grid[i][j]=None

        while q:
            i,j=q.popleft()
            for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                vi,vj=i+di,j+dj
                if 0<=vi<m and 0<=vj<n and grid[vi][vj] is None:
                        grid[vi][vj]=grid[i][j]+1
                        q.append((vi,vj))
        
        return grid


        
        
        
        