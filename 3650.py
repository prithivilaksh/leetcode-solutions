# class Solution:
#     def minCost(self, n: int, edges: List[List[int]]) -> int:

#         g=defaultdict(list)
#         for u,v,w in edges:
#             g[u].append((v,w))
#             g[v].append((u,2*w))

#         q=[(0,0)]
#         vis=[False]*n

#         while q:
#             w,u=heappop(q)
#             if vis[u]: continue
#             if u==n-1: return w
#             vis[u]=True
#             for v,nw in g[u]:
#                 if not vis[v]:
#                     heappush(q,(w+nw,v))
                    
#         return -1

# class Solution:
#     def minCost(self, n: int, edges: List[List[int]]) -> int:

#         g=defaultdict(list)
#         for u,v,w in edges:
#             g[u].append((v,w))
#             g[v].append((u,2*w))

#         dis=[inf]*n
#         q,dis[0]=[(0,0)],0

#         while q:
#             w,u=heappop(q)
#             if w>dis[u]: continue
#             if u==n-1: return w
#             for v,nw in g[u]:
#                 if w+nw < dis[v]:
#                     dis[v]=w+nw
#                     heappush(q,(w+nw,v))
                    
#         return -1


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        g=[defaultdict(lambda: inf) for _ in range(n)]
        for u,v,w in edges:
            g[u][v]=min(g[u][v],w)
            g[v][u]=min(g[v][u],2*w)

        dis=[inf]*n
        q,dis[0]=[(0,0)],0

        while q:
            w,u=heappop(q)
            if w>dis[u]: continue
            if u==n-1: return w
            for v,nw in g[u].items():
                if w+nw < dis[v]:
                    dis[v]=w+nw
                    heappush(q,(w+nw,v))
                    
        return -1
            