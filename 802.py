# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
#         g=defaultdict(list)
#         n=len(graph)
#         indeg=[0]*n

#         for u,nei in enumerate(graph):
#             for v in nei:
#                 g[v].append(u)
#                 indeg[u]+=1
        
#         dq=deque([i for i in range(n) if indeg[i]==0])
#         res=[]
#         while dq:
#             u=dq.popleft()
#             res.append(u)
#             for v in g[u]:
#                 indeg[v]-=1
#                 if indeg[v]==0: dq.append(v)
#         return sorted(res)


# class Solution:
#     def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        
#         g={u:nei for u,nei in enumerate(g)}
#         def dfs(u):
#             if u not in g: return False
#             vis.add(u)
#             for v in g[u]:
#                 if v in vis or dfs(v): return True
            
#             vis.discard(u)
#             del g[u]
#             return False
        
#         n,vis,res=len(g),set(),[]
#         for i in range(n):
#             if i in vis: continue
#             dfs(i)
#         for i in range(n):
#             if i in vis: continue
#             res.append(i)
#         return res

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        
        def dfs(u):
            if g[u]==-1: return False
            vis.add(u)
            for v in g[u]:
                if v in vis or dfs(v): return True
            
            vis.discard(u)
            g[u]=-1
            return False
        
        n,vis,res=len(g),set(),[]
        for i in range(n):
            if i in vis: continue
            dfs(i)
            if g[i]==-1: res.append(i)
        return res

