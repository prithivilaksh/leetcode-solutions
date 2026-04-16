# redo
# class Solution:
#     def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        

#         g=defaultdict(list)

#         for u,v in edges:
#             g[u].append((v,0))
#             g[v].append((u,1))
        
#         def dfs1(u,p):
#             res=0
#             for v,w in g[u]:
#                 if v==p: continue
#                 below[v]+=dfs1(v,u)
#                 res+=w+below[v]
#             return res
        
#         res,below=[0]*n,[0]*n
#         res[0]=below[0]=dfs1(0,-1)

#         def dfs2(u,p):
#             for v,w in g[u]:
#                 if v==p: continue
#                 res[v]=below[v]+ (res[u]-below[v]) + (1 if w==0 else -1)
#                 dfs2(v,u)
        
#         dfs2(0,-1)
#         return res

# class Solution:
#     def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        

#         g=defaultdict(list)

#         for u,v in edges:
#             g[u].append((v,0))
#             g[v].append((u,1))
        
#         def dfs1(u,p):
#             res=0
#             for v,w in g[u]:
#                 if v==p: continue
#                 res+=w+dfs1(v,u)
#             return res
        
#         res=[0]*n
#         res[0]=dfs1(0,-1)

#         def dfs2(u,p):
#             for v,w in g[u]:
#                 if v==p: continue
#                 res[v]=res[u] + (1 if w==0 else -1)
#                 dfs2(v,u)
        
#         dfs2(0,-1)
#         return res


# class Solution:
#     def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:

#         graph = [[] for _ in range(n)]
#         for u, v in edges:
#             graph[u].append((v, 0))
#             graph[v].append((u, 1))


#         cost = [0] * n
#         depth = [0] * n
#         visited = [False] * n
#         visited[0] = True
#         total_cost = 0

#         queue = deque([0])
#         while queue:
#             u = queue.popleft()
#             for v, w in graph[u]:
#                 if visited[v]: continue
#                 visited[v] = True
#                 cost[v] = cost[u] + w
#                 depth[v] = depth[u] + 1
#                 total_cost += w  # each tree edge counted exactly once
#                 queue.append(v)

#         # For every node v:
#         #   ans[v] = total_cost + cost(v→0) - cost(0→v)
#         #          = total_cost + (depth[v] - cost[v]) - cost[v]
#         #          = total_cost + depth[v] - 2 * cost[v]
#         return [total_cost + depth[v] - 2 * cost[v] for v in range(n)]


# class Solution:
#     def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        
#         g=defaultdict(list)
#         cost=[0]*n

#         for u,v in edges:
#             g[u].append((v,0))
#             g[v].append((u,1))
        
#         def dfs1(u,p):
#             for v,c in g[u]:
#                 if v==p: continue
#                 cost[u]+=c+dfs1(v,u)
#             return cost[u]
#         dfs1(0,-1)

#         def dfs2(u,p):
#             for v,c in g[u]:
#                 if v==p: continue
#                 cost[v]=cost[u]+ (1 if c==0 else -1)
#                 dfs2(v,u)
#         dfs2(0,-1)
#         return cost
            

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        
        g=defaultdict(list)
        dis,rev=[0]*n,[0]*n

        for u,v in edges:
            g[u].append((v,0))
            g[v].append((u,1))
        
        def dfs(u,p,d):
            res=0
            for v,c in g[u]:
                if v==p: continue
                dis[v]=d+1
                rev[v]=rev[u]+c
                res+=c+dfs(v,u,d+1)
            return res
        tot=dfs(0,-1,0)

        return [tot+dis[i]-2*rev[i] for i in range(n)]
            
