# class Solution:
#     def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
#         g=defaultdict(list)
#         for u,v in edges:
#             g[u].append(v)
#             g[v].append(u)
        
#         dp=defaultdict(bool)
#         def dfs(l,r,used):
#             used|=1<<l
#             used|=1<<r
#             if dp[used]: return dp[used]
#             res=0
#             vis[l]=vis[r]=True
#             for u in g[l]:
#                 if not vis[u]:
#                     for v in g[r]:
#                         if not vis[v] and u!=v and label[u]==label[v]:
#                             res=max(res,2+dfs(u,v,used))
#             vis[l]=vis[r]=False
#             dp[used]=res
#             return res

#         res=0
#         vis=[False]*n
#         for u in range(n):
#             res=max(res,1+dfs(u,u,0))
#             for v in g[u]:
#                 if u<v and label[u]==label[v]:
#                     res=max(res,2+dfs(u,v,0))
        
#         return res

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        dp=defaultdict(lambda: -1)
        def dfs(l,r,used):
            used|=1<<l
            used|=1<<r
            if dp[(l,r,used)]!=-1: 
                return dp[used]
            res=0
            for u in g[l]:
                if (used>>u & 1)==0:
                    for v in g[r]:
                        if (used>>v & 1)==0 and u!=v and label[u]==label[v]:
                            res=max(res,2+dfs(min(u,v),max(u,v),used))
            dp[(l,r,used)]=res
            return res

        res=0
        for u in range(n):
            res=max(res,1+dfs(u,u,0))
            for v in g[u]:
                if u<v and label[u]==label[v]:
                    res=max(res,2+dfs(u,v,0))
        
        return res


# 16 8421
# 1. 1111