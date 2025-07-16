# class Solution:
#     def minDays(self, grid: List[List[int]]) -> int:

#         m,n=len(grid),len(grid[0])
#         self.lookfor=0
#         def dfs(ui,uj):
#             grid[ui][uj]=self.lookfor+1
#             for di,dj in ((1,0),(0,1),(0,-1),(-1,0)):
#                 vi,vj=ui+di,uj+dj
#                 if 0<=vi<m and 0<=vj<n and grid[vi][vj]==self.lookfor:
#                     dfs(vi,vj)

#         def numOfIslands():
#             self.lookfor+=1
#             cc=0
#             for i in range(m):
#                 for j in range(n):
#                     if grid[i][j]==self.lookfor:
#                         dfs(i,j)
#                         cc+=1
#             return cc

#         cc=numOfIslands()
#         # if cc==0 or cc>=2: return 0
#         if cc!=1: return 0


#         res=inf
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]!=0:
#                     tmp=grid[i][j]
#                     grid[i][j]=0
#                     cc=numOfIslands()
#                     # if cc==0 or cc>=2: return 1
#                     if cc!=1: return 1
#                     grid[i][j]=tmp+1

#         return 2

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        # idea -> it takes atmost 2 days(or flips) to disconnect
        # cases
        # 1. if root has multiple mutually exclusive subgraphs then root is an articulation point.
        # 2. even if disc[u]<=low[v], u can still not be an articulation point (if u is the root).
        # 3. if there are 0 or >=2 components, no change is required.
        # 4. if there is only one 1 in grid, then it is an articulation point

        m,n=len(grid),len(grid[0])
        dis=[[-1]*n for i in range(m)]
        low=[[-1]*n for i in range(m)]

        def dfs(par,ui,uj):
            dis[ui][uj]=low[ui][uj]=self.time
            self.time+=1
            childSub=0
            for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                vi,vj=ui+di,uj+dj
                if 0<=vi<m and 0<=vj<n and grid[vi][vj]:
                    if par==(vi,vj) : continue
                    if dis[vi][vj]==-1:
                        childSub+=1
                        dfs((ui,uj),vi,vj)
                        low[ui][uj]=min(low[ui][uj],low[vi][vj])
                        if dis[ui][uj]<=low[vi][vj] and par!=(-1,-1): self.hasAP=1
                    else: low[ui][uj]=min(low[ui][uj],dis[vi][vj]) # low holds the smallest dis time of already visited(ancestral) node
            
            if par==(-1,-1) and childSub>1: self.hasAP=1

        cnt=cc=self.time=self.hasAP=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    cnt+=1
                    if dis[i][j]==-1:
                        cc+=1
                        dfs((-1,-1),i,j)
        
        # if cc==0 or cc>=2: return 0
        if cc!=1: return 0
        if cnt==1 or self.hasAP: return 1
        return 2