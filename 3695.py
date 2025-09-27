# class Solution:
#     def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        
#         n = len(nums)
#         g=defaultdict(list)
#         for u,v in swaps:
#             g[u].append(v)
#             g[v].append(u)
        
#         vis = [False] * n
#         res = 0
        
#         def dfs(u):
#             vis[u]=True
#             indices.append(u)
#             for v in g[u]:
#                 if not vis[v]:
#                     dfs(v)
        
#         for i in range(n):
#             if not vis[i]:
#                 indices = []
#                 dfs(i)
                
#                 values = [nums[j] for j in indices]
#                 values.sort(reverse=True)
                
#                 even_positions = sum(1 for j in indices if j % 2 == 0)
#                 odd_positions = len(indices) - even_positions
                
#                 idx = 0
#                 for _ in range(even_positions):
#                     res += values[idx]
#                     idx += 1
#                 for _ in range(odd_positions):
#                     res -= values[idx]
#                     idx += 1
                    
#         return res

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n,res=len(nums),0
        par=[i for i in range(n)]
        g=defaultdict(list)

        def find(x):
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        
        for u,v in swaps: par[find(u)]=find(v)

        for i in range(n): g[find(i)].append(i)
        
        for inds in g.values():
            vals=sorted(nums[i] for i in inds)
            odds=sum(i%2 for i in inds)
            res+=sum(vals[odds:])-sum(vals[:odds])
        return res