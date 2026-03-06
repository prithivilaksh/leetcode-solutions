# class Solution:
#     def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
#         g,res=defaultdict(set),0
#         for u,v in roads:
#             g[u].add(v)
#             g[v].add(u)
        
#         for i in range(n):
#             for j in range(i+1,n):
#                 nrank=len(g[i])+len(g[j]) - (i in g[j])
#                 res=max(res,nrank)
#         return res

# class Solution:
#     def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
#         g,res=defaultdict(set),0
#         for u,v in roads:
#             g[u].add(v)
#             g[v].add(u)
        
#         h=sorted([u for u in range(n)],reverse=True,key=lambda x: len(g[x]))
#         for i in range(n):
#             u=h[i]
#             if 2*len(g[u])<res: break
#             for j in range(i+1,n):
#                 v=h[j]
#                 nrank=len(g[u])+len(g[v]) - (u in g[v])
#                 if nrank<res: break
#                 res=max(res,nrank)
#         return res

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        g,res=defaultdict(set),0
        for u,v in roads:
            g[u].add(v)
            g[v].add(u)
        
        mx=max(len(g[x]) for x in range(n))
        first=[x for x in range(n) if len(g[x])==mx]
        if len(first)>1:
            for u in first:
                for v in first:
                    if u!=v and u not in g[v]: return 2*mx
            return 2*mx-1

        smx=max(len(g[x]) for x in range(n) if len(g[x])!=mx)
        second=[x for x in range(n) if len(g[x])==smx]  
        for u in first:
            for v in second:
                if u!=v and u not in g[v]: return mx+smx
        return mx+smx-1

