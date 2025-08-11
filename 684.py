# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         g=defaultdict(list)
#         for u,v in edges:
#             g[u].append(v)
#             g[v].append(u)
        
#         def dfs(u,prev):
#             vis[u]=True
#             for v in g[u]:
#                 if v!=prev and not vis[v]:
#                     dfs(v,u)

#         for u,v in edges[::-1]:
#             vis=defaultdict(bool)
#             dfs(u,v)
#             if vis[v]: return [u,v]
#         return []

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         g=defaultdict(list)
#         for u,v in edges:
#             g[u].append(v)
#             g[v].append(u)
        
#         dis=defaultdict(lambda :None)
#         low=defaultdict(lambda :None)
#         notres=[]
#         def dfs(u,time):
#             dis[u]=low[u]=time
#             for v in g[u]:
#                 if dis[v]==None:
#                     dfs(v,time+1)
#                     if time==low[v]:notres.append([min(u,v),max(u,v)])
#                     low[u]=min(low[u],low[v])
#                 else :
#                     low[u]=min(low[u],dis[v])
        
#         dfs(1,0)
#         for u,v in edges[::-1]:
#             if [min(u,v),max(u,v)] in notres: continue
#             return [u,v]
#         return []


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         g=defaultdict(list)
#         for u,v in edges:
#             g[u].append(v)
#             g[v].append(u)
        
#         dis=defaultdict(lambda :None)
#         low=defaultdict(lambda :None)
#         notres=[]
#         def dfs(u,par,time):
#             dis[u]=low[u]=time
#             for v in g[u]:
#                 if v==par: continue
#                 if dis[v]==None:
#                     dfs(v,u,time+1)
#                     if time+1==low[v]:notres.append([min(u,v),max(u,v)])
#                     low[u]=min(low[u],low[v])
#                 else :
#                     low[u]=min(low[u],dis[v])
        
#         dfs(1,-1,0)
#         for u,v in edges[::-1]:
#             if [min(u,v),max(u,v)] in notres: continue
#             return [u,v]
#         return []


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         def dfs(u,par,t):
#             if u==t: return True
#             for v in g[u]:
#                 if v!=par and dfs(v,u,t): return True
#             return False
        
#         res=[]
#         g=defaultdict(list)
#         for u,v in edges:
#             if dfs(u,-1,v):res=[u,v]
#             else: 
#                 g[u].append(v)
#                 g[v].append(u)
        
#         return res

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         def dfs(u,par,t):
#             if u==t: return True
#             for v in g[u]:
#                 if v!=par and dfs(v,u,t): return True
#             return False
        
#         g=defaultdict(list)
#         for u,v in edges:
#             if dfs(u,-1,v):return [u,v]
#             else: 
#                 g[u].append(v)
#                 g[v].append(u)
        
#         return [res]


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         def dfs(u,t):
#             if u==t: return True
#             vis[u]=True
#             for v in g[u]:
#                 if not vis[v] and dfs(v,t): return True
#             return False
        
#         res=[]
#         g=defaultdict(list)
#         for u,v in edges:
#             vis=defaultdict(bool)
#             if dfs(u,v):res=[u,v]
#             else: 
#                 g[u].append(v)
#                 g[v].append(u)
        
#         return res

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         n=len(edges)
#         par=[x for x in range(n+1)]
#         def find(x):
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a,b=find(a),find(b)
#             par[b]=a
#             return a==b
        
#         res=[]
#         for u,v in edges:
#             if union(u,v):res=[u,v]
        
#         return res


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[x for x in range(n+1)]
        def find(x):
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        
        def union(a,b):
            a,b=find(a),find(b)
            par[b]=a
            return a==b
        
        for u,v in edges:
            if union(u,v):return [u,v]
        
        return []