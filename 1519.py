# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
#         g=defaultdict(list)
#         res=[0]*n
#         for a,b in edges:
#             g[a].append(b)
#             g[b].append(a)

#         def dfs(u,p):

#             l2c=defaultdict(int,{labels[u]:1})
#             for v in g[u]:
#                 if v==p: continue
#                 for k,v in dfs(v,u).items():
#                     l2c[k]+=v
#             res[u]=l2c[labels[u]]
#             return l2c

#         dfs(0,-1)
#         return res


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        g=defaultdict(list)
        cnt=defaultdict(int)
        res=[0]*n
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(u,p):
            before=cnt[labels[u]]
            for v in g[u]:
                if v==p: continue
                dfs(v,u)
            cnt[labels[u]]+=1
            res[u]=cnt[labels[u]]-before

        dfs(0,-1)
        return res