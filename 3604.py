# class Solution:
#     def minTime(self, n: int, edges: List[List[int]]) -> int:

#         g=defaultdict(list)

#         for [u,v,s,e] in edges:
#             g[u].append([s,e,v])

#         mt=[inf]*n

#         q=[[0,0]]
#         while q:
#             [time,u]=heapq.heappop(q)
#             if u==n-1: return time
#             if time >= mt[u]: continue
#             mt[u]=time
#             for [s,e,v] in g[u]:
#                 if s<=time<=e: heapq.heappush(q,[time+1,v])
#                 elif time<s: heapq.heappush(q,[s+1,v])

#         return -1 

# class Solution:
#     def minTime(self, n: int, edges: List[List[int]]) -> int:

#         g=defaultdict(list)
#         for [u,v,s,e] in edges:
#             g[u].append([s,e,v])

#         vis,q=[False]*n,[[0,0]]
#         while q:
#             [time,u]=heappop(q)
#             if vis[u]: continue
#             if u==n-1: return time
#             vis[u]=True
#             for [s,e,v] in g[u]:
#                 if s<=time<=e: heappush(q,[time+1,v])
#                 elif time<s: heappush(q,[s+1,v])

#         return -1 

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:

        g=defaultdict(list)
        for [u,v,s,e] in edges:
            g[u].append([s,e,v])

        vis,q=[False]*n,[[0,0]]
        while q:
            [time,u]=heappop(q)
            if vis[u]: continue
            if u==n-1: return time
            vis[u]=True
            for [s,e,v] in g[u]:
                if not vis[v]:
                    if s<=time<=e: heappush(q,[time+1,v])
                    elif time<s: heappush(q,[s+1,v])

        return -1 