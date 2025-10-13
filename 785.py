# class Solution:
#     def isBipartite(self, g: List[List[int]]) -> bool:
        
#         def isBP(u,c):
#             color[u]=c
#             for v in g[u]:
#                 if color[v]==c: return False
#                 elif color[v]==-1 and not isBP(v,not c): return False
#             return True

#         color=defaultdict(lambda: -1)
#         for u in range(len(g)):
#             if color[u]==-1 and not isBP(u,0): return False
#         return True

class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        
        def isBP(u,c):
            color[u]=c
            dq=deque([u])
            while dq:
                u=dq.popleft()
                for v in g[u]:
                    if color[v]==color[u]: return False
                    if color[v]==-1: color[v]=color[u]^1;dq.append(v)
            return True

        color=defaultdict(lambda: -1)
        for u in range(len(g)):
            if color[u]==-1 and not isBP(u,0): return False
        return True