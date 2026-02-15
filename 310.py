# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if not edges: return [0]
#         g=defaultdict(set)
        
#         for u,v in edges: 
#             g[u].add(v);g[v].add(u)
        
#         dq=deque()
#         for i in range(n):
#             if len(g[i])==1: dq.append(i)

#         res=[]
#         while dq:
#             res=[]
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 res.append(u)
#                 while g[u]:
#                     v=g[u].pop()
#                     g[v].remove(u)
#                     if len(g[v])==1: dq.append(v)
        
#         return res

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        g=defaultdict(set)
        
        for u,v in edges: 
            g[u].add(v);g[v].add(u)
        
        dq=deque()
        for i in range(n):
            if len(g[i])==1: dq.append(i)

        while n>2:
            n-=len(dq)
            for _ in range(len(dq)):
                u=dq.popleft()
                while g[u]:
                    v=g[u].pop()
                    g[v].remove(u)
                    if len(g[v])==1: dq.append(v)
        
        return list(dq)