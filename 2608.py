# WA
# class Solution:
#     def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        
#         g,res=defaultdict(list),[inf]
#         path,vis=[],set()
#         for u,v in edges:
#             g[u].append(v)
#             g[v].append(u)

#         def dfs(u,prev):
#             if u in vis: 
#                 print(u,vis,path)
#                 if u in path:
#                     res[0]=min(res[0],len(path)-path.index(u))
#                 return
#             vis.add(u)
#             path.append(u)
#             for v in g[u]:
#                 if v!=prev: dfs(v,u)
#             path.pop()
        
#         for u in range(n):
#             if u not in vis:
#                 dfs(u,-1) 
        
#         return -1 if res[0]==inf else res[0]



# class Solution:
#     def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        
#         g,res=defaultdict(list),[inf]
#         dis,vis=[inf]*n,set()
#         for u,v in edges:
#             g[u].append(v)
#             g[v].append(u)

#         def dfs(u,prev,d):
#             if dis[u]!=inf:
#                 if d>dis[u]+1: 
#                     res[0]=min(res[0],d-dis[u])
#                     return
#                 elif d<dis[u]: pass
#                 else: return
#             dis[u]=d
#             for v in g[u]:
#                 if v!=prev: dfs(v,u,d+1)
        
#         for u in range(n):
#             if dis[u]==inf: dfs(u,-1,0) 
        
#         return -1 if res[0]==inf else res[0]



class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        
        g,res=defaultdict(list),inf
        res,d=[inf],[inf]*n
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u,par,cd):
            d[u]=cd 
            for v in g[u]:
                if v==par: continue
                if cd+1<d[v]: dfs(v,u,cd+1)
                # elif d[v]+1<cd: res[0]=min(res[0],cd+1-d[v])
                elif d[v]<cd: res[0]=min(res[0],cd+1-d[v])
        
        for u in range(n):
            if d[u]==inf: dfs(u,-1,0)
        
        return -1 if res[0]==inf else res[0]


# cd+1>=d[v]<=cd-1