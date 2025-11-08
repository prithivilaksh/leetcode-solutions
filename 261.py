# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         if len(edges) != (n - 1): return False

#         adj = [[] for _ in range(n)]
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)

#         visit = set()
#         def dfs(node, par):
#             if node in visit:
#                 return False

#             visit.add(node)
#             for nei in adj[node]:
#                 if nei == par:
#                     continue
#                 if not dfs(nei, node):
#                     return False
#             return True

#         return dfs(0, -1) and len(visit) == n

class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False

        self.comps -= 1
        self.Parent[pv] = pu
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v): return False
        return dsu.components() == 1