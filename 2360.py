# class Solution:
#     def longestCycle(self, edges: List[int]) -> int:
        
#         n=len(edges)
#         res=[-1]

#         def dfs(u):
#             if edges[u]==-2: return u,1
#             v=edges[u]
#             edges[u]=-2
#             if v!=-1:
#                 end,dis=dfs(v)
#                 if end==u: res[0]=max(res[0],dis)
#                 else: return end,dis+1
            
#             return -1,-1

#         for u in range(n):
#             if edges[u]>0: dfs(u)
#         return res[0]


# class Solution:
#     def longestCycle(self, nei: List[int]) -> int:

#         n,self.res=len(nei),-1
#         vis=[False]*n

#         def dfs(u):
#             vis[u]=True
#             path.append(u)
#             v=nei[u]
#             if v==-1: return
#             if vis[v]: 
#                 for i,x in enumerate(path):
#                     if x==v: self.res=max(self.res,len(path)-i);break
#             else: dfs(v)

#         for i in range(n):
#             if not vis[i]:
#                 path=[]
#                 dfs(i)
#         return self.res
        


# class Solution:
#     def longestCycle(self, to: List[int]) -> int:
        
#         n,res=len(to),-1
#         for u in range(n):
#             path=[]
#             while to[u]!=-1:
#                 path.append(u)
#                 v=to[u]
#                 to[u]=-1
#                 u=v
#             if u in path:
#                 res=max(res,len(path)-path.index(u))
#         return res


class Solution:
    def longestCycle(self, to: List[int]) -> int:
        
        n,res=len(to),-1
        for u in range(n):
            path=[]
            while to[u]!=-1:
                path.append(u)
                to[u],u=-1,to[u]

            if u in path:
                res=max(res,len(path)-path.index(u))
        return res

