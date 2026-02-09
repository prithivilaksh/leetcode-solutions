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



class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        par,rank={},{}
        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(a,b):
            a,b=find(a),find(b)
            if a==b: return
            if rank[a]>=rank[b]:a,b=b,a
            rank[b]+=rank[a]
            par[a]=b
        
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    par[(i,j)],rank[(i,j)]=(i,j),1
                    if i-1>=0 and grid[i-1][j]==1: union((i,j),(i-1,j))
                    if j-1>=0 and grid[i][j-1]==1: union((i,j),(i,j-1))
        
        if len(rank) == 0: return 1
        if len(rank) == 1: return min(n*n, next(iter(rank.values())) + 1)
        
        res=max(rank.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    parents,tot=set(),1
                    for x,y in (i-1,j),(i,j+1),(i,j-1),(i+1,j):
                        if 0<=x<n and 0<=y<n and grid[x][y]==1:
                            parents.add(find((x,y)))
                    for c in parents: tot+=rank[c]
                    res=max(res,tot)
        
        return res



