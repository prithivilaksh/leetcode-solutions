# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:

#         def bfs(T):#can do dfs as well
#             if grid[0][0]>T: return False
#             vis=set((0,0))
#             q=[(0,0)]
#             for i,j in q:
#                 if i==n-1==j: return True
#                 for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                     vi,vj=i+di,j+dj
#                     if 0<=vi<n and 0<=vj<n and (vi,vj) not in vis and grid[vi][vj]<=T:
#                         vis.add((vi,vj))
#                         q.append((vi,vj))

#         n=len(grid)
#         l,r,res=0,(n*n)+1,0
#         while l<=r:
#             m=l+(r-l)//2
#             if bfs(m): res=m;r=m-1
#             else: l=m+1
#         return res

# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
        
#         n=len(grid)
#         q=[(grid[0][0],0,0)]
#         grid[0][0]=-1

#         res=0
#         while q:
#             h,i,j=heappop(q)

#             res=max(res,h)
#             if i==n-1==j: return res

#             for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<n and 0<=vj<n and grid[vi][vj]!=-1:
#                     heappush(q,(grid[vi][vj],vi,vj))
#                     grid[vi][vj]=-1
        
#         return "X"

# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:

#         def bfs(T):
#             if grid[0][0]>T: return False
#             q,vis=[(0,0)],set((0,0))
#             for i,j in q:
#                 if i==n-1==j: return True
#                 for di,dj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
#                     if 0<=di<n and 0<=dj<n and (di,dj) not in vis and grid[di][dj]<=T:
#                         vis.add((di,dj))
#                         q.append((di,dj))

#         n=len(grid)
#         l,r=0,(n*n)+1
#         while l<r:
#             m=l+(r-l)//2
#             if bfs(m): r=m
#             else: l=m+1
#         return r

# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         n=len(grid)
#         h=[(grid[0][0],0,0)];grid[0][0]=-1
#         while h:
#             ele,i,j=heappop(h)
#             if i==j==n-1: return ele
#             for di,dj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
#                 if 0<=di<n and 0<=dj<n and grid[di][dj]!=-1:
#                     heappush(h,(max(ele,grid[di][dj]),di,dj))
#                     grid[di][dj]=-1
#         return -1


# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
        
#         n=len(grid)
#         h=[(grid[0][0],0,0)]

#         while True:
#             t,i,j=heappop(h)
#             if i==n-1==j: return t
#             if grid[i][j]==-1: continue

#             for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                 vi,vj=i+di,j+dj
#                 if 0<=vi<n and 0<=vj<n and grid[vi][vj]!=-1:
#                     heappush(h,(max(t,grid[vi][vj]),vi,vj))

#             grid[i][j]=-1

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        h=[(grid[0][0],0,0)];grid[0][0]=-1

        while True:
            t,i,j=heappop(h)
            if i==n-1==j: return t

            for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                vi,vj=i+di,j+dj
                if 0<=vi<n and 0<=vj<n and grid[vi][vj]!=-1:
                    heappush(h,(max(t,grid[vi][vj]),vi,vj)) # the first path is the best path because t is always minimum and grid[vi][vj] is constant
                    grid[vi][vj]=-1
