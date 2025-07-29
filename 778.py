# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:

#         def bfs(T):#can do dfs as well
#             vis=set((0,0))
#             q=[(0,0)]
#             for i,j in q:
#                 if grid[i][j]>T: continue
#                 if i==n-1==j: return True
#                 for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                     vi,vj=i+di,j+dj
#                     if 0<=vi<n and 0<=vj<n and (vi,vj) not in vis:
#                         vis.add((vi,vj))
#                         q.append((vi,vj))

#         n=len(grid)
#         l,r,res=0,(n*n)+1,0
#         while l<=r:
#             m=l+(r-l)//2
#             if bfs(m): res=m;r=m-1
#             else: l=m+1
#         return res

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        q=[(grid[0][0],0,0)]
        grid[0][0]=-1

        res=0
        while q:
            h,i,j=heappop(q)

            res=max(res,h)
            if i==n-1==j: return res

            for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                vi,vj=i+di,j+dj
                if 0<=vi<n and 0<=vj<n and grid[vi][vj]!=-1:
                    heappush(q,(grid[vi][vj],vi,vj))
                    grid[vi][vj]=-1
        
        return "X"