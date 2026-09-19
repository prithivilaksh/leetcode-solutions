# class Solution:
#     def maximumDetonation(self, bombs: list[list[int]]) -> int:
        
#         def can_detonate(a,b):
#             dis=(a[0]-b[0])**2+(a[1]-b[1])**2
#             return dis<=a[2]**2
        
#         n=len(bombs)
#         g=defaultdict(list)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if can_detonate(bombs[i],bombs[j]): g[i].append(j)
#                 if can_detonate(bombs[j],bombs[i]): g[j].append(i)
        
#         def dfs(u):
#             vis.add(u)
#             for v in g[u]:
#                 if v not in vis: dfs(v)
        
#         res=0
#         for i in range(n):
#             vis=set()
#             dfs(i)
#             res=max(res,len(vis))
        
#         return res


# class Solution:
#     def maximumDetonation(self, bombs: list[list[int]]) -> int:
        
#         def can_detonate(a,b):
#             dis=(a[0]-b[0])**2+(a[1]-b[1])**2
#             return dis<=a[2]**2
        
#         n=len(bombs)
#         g,indeg=defaultdict(list),defaultdict(int)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if can_detonate(bombs[i],bombs[j]): g[i].append(j)
#                 if can_detonate(bombs[j],bombs[i]): g[j].append(i)
        
#         def dfs(u):
#             vis.add(u)
#             for v in g[u]:
#                 if v not in vis: dfs(v)
        
#         res,gvis=0,set()
#         for i in sorted(range(n),key=lambda x:len(g[x])):
#             if i in gvis: continue
#             vis=set()
#             dfs(i)
#             res=max(res,len(vis))
#             gvis.update(vis)
        
#         return res


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        
        def can_detonate(a,b):
            dis=(a[0]-b[0])**2+(a[1]-b[1])**2
            return dis<=a[2]**2
        
        n=len(bombs)
        g,indeg=defaultdict(list),defaultdict(int)
        for i in range(n-1):
            for j in range(i+1,n):
                if can_detonate(bombs[i],bombs[j]): g[i].append(j)
                if can_detonate(bombs[j],bombs[i]): g[j].append(i)
        
        def dfs(u):
            vis.add(u)
            for v in g[u]:
                if v not in vis: dfs(v)
        
        res,gvis=0,set()
        # for i in sorted(range(n),key=lambda x:len(g[x]),reverse=True):
        for i in range(n):
            if i in gvis: continue
            vis=set()
            dfs(i)
            res=max(res,len(vis))
            gvis.update(vis)
        
        return res
