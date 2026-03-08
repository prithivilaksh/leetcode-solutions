# class Solution:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
#         m,n=len(grid),len(grid[0])
#         ui=uj=l0=0
#         vis=set()
#         res=[0]
        
#         def dfs(i,j):
#             if grid[i][j]==2:
#                 if len(vis)==l0+1: res[0]+=1
#                 return
#             vis.add((i,j))
#             for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<m and 0<=vj<n and (vi,vj) not in vis and grid[vi][vj]!=-1:
#                     dfs(vi,vj)

#             vis.remove((i,j))
        

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==0:l0+=1
#                 elif grid[i][j]==1:ui,uj=i,j
#         dfs(ui,uj)
#         return res[0]

# class Solution:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
#         m,n=len(grid),len(grid[0])
#         ui=uj=l0=0
#         vis=set()
#         res=[0]
        
#         def dfs(i,j):
#             if grid[i][j]==2:
#                 if len(vis)==l0+2: res[0]+=1
#                 return
#             for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<m and 0<=vj<n and (vi,vj) not in vis and grid[vi][vj]!=-1:
#                     vis.add((vi,vj))
#                     dfs(vi,vj)
#                     vis.remove((vi,vj))

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==0:l0+=1
#                 elif grid[i][j]==1:ui,uj=i,j
#         vis.add((ui,uj))
#         dfs(ui,uj)
#         return res[0]




# class Solution:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
#         m,n=len(grid),len(grid[0])
#         ui=uj=l0=0
#         res=[0]
        
#         def dfs(i,j,cnt):

#             for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<m and 0<=vj<n and grid[vi][vj]!=-1:
#                     if grid[vi][vj]==2:
#                         if l0==cnt: res[0]+=1
#                         continue
#                     grid[vi][vj]=-1
#                     dfs(vi,vj,cnt+1)
#                     grid[vi][vj]=0

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==0:l0+=1
#                 elif grid[i][j]==1:ui,uj=i,j

#         grid[ui][uj]=-1
#         dfs(ui,uj,0)
#         return res[0]



# class Solution:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:

#         m,n,cnt,res,vis=len(grid),len(grid[0]),0,[0],set()
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==0: cnt+=1
#                 elif grid[i][j]==1: start=(i,j)
#                 elif grid[i][j]==2: end=(i,j)

#         def dfs(d,i,j):
#             if i<0 or i==m or j<0 or j==n or grid[i][j]==-1 or (i,j) in vis: return
#             if (i,j)==end :
#                 if d==cnt+1: res[0]+=1
#                 return
#             vis.add((i,j))
#             dfs(d+1,i+1,j)
#             dfs(d+1,i-1,j)
#             dfs(d+1,i,j+1)
#             dfs(d+1,i,j-1)
#             vis.discard((i,j))
#         dfs(0,*start)
#         return res[0]


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        m,n,cnt,res=len(grid),len(grid[0]),0,[0]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0: cnt+=1
                elif grid[i][j]==1: start=(i,j)

        def dfs(d,i,j):
            if i<0 or i==m or j<0 or j==n or grid[i][j]==-1: return
            if grid[i][j]==2:
                if d==cnt+1: res[0]+=1
                return
            grid[i][j]=-1
            dfs(d+1,i+1,j);dfs(d+1,i-1,j)
            dfs(d+1,i,j+1);dfs(d+1,i,j-1)
            grid[i][j]=0
        dfs(0,*start)
        return res[0]














