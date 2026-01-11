# class Solution:
#     def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
#         dir=((-1,-1),(-1,1),(1,1),(1,-1))

#         @cache
#         def dp(i,j,d,rem):
#             res=1
#             if rem==1:
#                 vd=(d+1)%4
#                 di,dj=dir[vd]
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<m and 0<=vj<n and grid[i][j]+grid[vi][vj]==2:
#                     res=max(res,1+dp(vi,vj,vd,0))
            
#             vd=d
#             di,dj=dir[vd]
#             vi,vj=i+di,j+dj
#             if 0<=vi<m and 0<=vj<n and grid[i][j]+grid[vi][vj]==2:
#                 res=max(res,1+dp(vi,vj,vd,rem))            

#             return res

#         m,n,res=len(grid),len(grid[0]),0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     res=max(res,1)
#                     for d,(di,dj) in enumerate(dir):
#                         vi,vj=i+di,j+dj
#                         if 0<=vi<m and 0<=vj<n and grid[vi][vj]==2:
#                             res=max(res,1+dp(vi,vj,d,1))
        
#         return res


# class Solution:
#     def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
#         dir=((-1,-1),(-1,1),(1,1),(1,-1))

#         @cache
#         def dp(i,j,d,rem):
#             res=1
#             for vd,nrem in ((d,rem),(d+1,rem-1)):
#                 vd%=4
#                 di,dj=dir[vd]
#                 vi,vj=i+di,j+dj
#                 if nrem>=0 and 0<=vi<m and 0<=vj<n and grid[i][j]+grid[vi][vj]==2:
#                     res=max(res,1+dp(vi,vj,vd,nrem))           

#             return res

#         m,n,res=len(grid),len(grid[0]),0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     res=max(res,1)
#                     for d,(di,dj) in enumerate(dir):
#                         vi,vj=i+di,j+dj
#                         if 0<=vi<m and 0<=vj<n and grid[vi][vj]==2:
#                             res=max(res,1+dp(vi,vj,d,1))
        
#         return res

# class Solution:
#     def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
#         dir=((-1,-1),(-1,1),(1,1),(1,-1))

#         @cache
#         def dp(i,j,d,rem):
#             res=1
#             vi,vj=dir[d][0]+i,dir[d][1]+j
#             if 0<=vi<m and 0<=vj<n and grid[i][j]+grid[vi][vj]==2:
#                 res=max(res,1+dp(vi,vj,d,rem))
            
#             if rem==1:
#                 d=(d+1)%4
#                 vi,vj=dir[d][0]+i,dir[d][1]+j
#                 if 0<=vi<m and 0<=vj<n and grid[i][j]+grid[vi][vj]==2:
#                     res=max(res,1+dp(vi,vj,d,0))        

#             return res

#         m,n,res=len(grid),len(grid[0]),0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     res=max(res,1)
#                     for d,(di,dj) in enumerate(dir):
#                         vi,vj=i+di,j+dj
#                         if 0<=vi<m and 0<=vj<n and grid[vi][vj]==2:
#                             res=max(res,1+dp(vi,vj,d,1))
        
#         return res

# class Solution:
#     def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
#         dir=((-1,-1),(-1,1),(1,1),(1,-1))
#         nxt=(2,2,0)

#         @cache
#         def dp(i,j,d,rem,t):
#             if i<0 or i==m or j<0 or j==n or grid[i][j]!=t: return 0
            
#             res=1+dp(i+dir[d][0],j+dir[d][1],d,rem,nxt[t])
#             if rem>0:
#                 d=(d+1)%4
#                 res=max(res,1+dp(i+dir[d][0],j+dir[d][1],d,rem-1,nxt[t]))
                
#             return res

#         m,n,res=len(grid),len(grid[0]),0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     for d in range(4):
#                         res=max(res,dp(i,j,d,1,1))
        
#         return res


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = (1, 1), (1, -1), (-1, -1), (-1, 1)
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, k, turn , target):
            i += DIRS[k][0]
            j += DIRS[k][1]
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != target:
                return 0
            ans = dfs(i, j, k, turn, 2 - target) + 1
            if turn:
                maxs = (m - i, j + 1, i + 1, n - j)
                k = (k + 1) % 4
                if maxs[k] > ans:
                    ans = max(ans, dfs(i, j, k, False, 2 - target) + 1)
            return ans
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                maxs = (m - i, j + 1, i + 1, n - j)
                for k, mx in enumerate(maxs): 
                    if mx > ans:
                        ans = max(ans, dfs(i, j, k, True, 2) + 1)
        
        return ans