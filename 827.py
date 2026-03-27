# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         par={}
#         rank=defaultdict(lambda:1)
#         zeros=[]
#         def find(x):
#             if par[x]!=x:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a=find(a)
#             b=find(b)
#             if a==b: return
#             if rank[a]>=rank[b]:a,b=b,a
#             rank[b]+=rank[a]
#             par[a]=b
        
#         n,default=len(grid),0
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j]==0: zeros.append((i,j))
#                 else:
#                     default=1
#                     par[(i,j)],rank[(i,j)]=(i,j),1
#                     if i-1>=0 and grid[i-1][j]==1: union((i,j),(i-1,j))
#                     if j-1>=0 and grid[i][j-1]==1: union((i,j),(i,j-1))
        
#         if len(rank) == 0: return 1
#         if len(rank) == 1: return min(n*n, next(iter(rank.values())) + 1)
        
#         res=max(rank.values(),default=default)
#         while zeros:
#             i,j=zeros.pop()
#             parents,tot=set(),1
#             for x,y in (i-1,j),(i,j+1),(i,j-1),(i+1,j):
#                 if 0<=x<n and 0<=y<n and grid[x][y]==1:
#                     parents.add(find((x,y)))
#             for c in parents:
#                 tot+=rank[c]
#             res=max(res,tot)
        
#         return res



# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         par,rank={},{}
#         def find(x):
#             if par[x]!=x:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a,b=find(a),find(b)
#             if a==b: return
#             if rank[a]>=rank[b]:a,b=b,a
#             rank[b]+=rank[a]
#             par[a]=b
        
#         n=len(grid)
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     par[(i,j)],rank[(i,j)]=(i,j),1
#                     if i-1>=0 and grid[i-1][j]==1: union((i,j),(i-1,j))
#                     if j-1>=0 and grid[i][j-1]==1: union((i,j),(i,j-1))
        
#         if len(rank) == 0: return 1
#         if len(rank) == 1: return min(n*n, next(iter(rank.values())) + 1)
        
#         res=max(rank.values())
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j]==0:
#                     parents,tot=set(),1
#                     for x,y in (i-1,j),(i,j+1),(i,j-1),(i+1,j):
#                         if 0<=x<n and 0<=y<n and grid[x][y]==1:
#                             parents.add(find((x,y)))
#                     for c in parents: tot+=rank[c]
#                     res=max(res,tot)
        
#         return res




# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
        
#         n,q,one=len(grid),[],0
#         par,rank={},defaultdict(lambda:1)

#         def find(x):
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]

#         def union(a,b):
#             a,b=find(a),find(b)
#             if a==b: return
#             if rank[a]<rank[b]: a,b=b,a
#             par[b]=a
#             rank[a]+=rank[b]

#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     par[(i,j)]=(i,j)
#                     one=1
#                     if i-1>=0 and grid[i-1][j]==1: union((i-1,j),(i,j))
#                     if j-1>=0 and grid[i][j-1]==1: union((i,j-1),(i,j))
#                 else: q.append((i,j))

#         res=max(rank.values(),default=one)
#         for i,j in q:
#             vis,cnt=set(),1
#             for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                 x,y=i+di,j+dj
#                 if 0<=x<n and 0<=y<n and grid[x][y]==1:
#                     nei=find((x,y))
#                     if nei in vis: continue
#                     vis.add(nei);cnt+=rank[nei]
#             res=max(res,cnt)
#         return res


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(i, j, index):
            if i<0 or i>=n or j<0 or j>=n or grid[i][j]!=1: return 0
            grid[i][j],area = index,1
            area += dfs(i+1, j, index)
            area += dfs(i-1, j, index)
            area += dfs(i, j+1, index)
            area += dfs(i, j-1, index)
            return area
        
        index = 2
        area_list = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area_list.append(dfs(i, j, index))
                    index += 1
        
        if not area_list: return 1
        ans = max(area_list)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    visited = []
                    new_area = 1
                    if i-1 >= 0 and grid[i-1][j] >= 2:
                        index = grid[i-1][j]
                        new_area += area_list[index-2]
                        visited.append(index)
                    if i+1 < n and grid[i+1][j] >= 2 and grid[i+1][j] not in visited:
                        index = grid[i+1][j]
                        new_area += area_list[index-2]
                        visited.append(index)
                    if j-1 >= 0 and grid[i][j-1] >= 2 and grid[i][j-1] not in visited:
                        index = grid[i][j-1]
                        new_area += area_list[index-2]
                        visited.append(index)
                    if j+1 < n and grid[i][j+1] >= 2 and grid[i][j+1] not in visited:
                        index = grid[i][j+1]
                        new_area += area_list[index-2]
                        visited.append(index)
                    ans = max(ans, new_area)
        
        return ans

        