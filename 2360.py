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

class Solution:
    def longestCycle(self, nei: List[int]) -> int:
        
        res,pos=-1,-100
        for i in range(len(nei)):
            u=i
            start=pos
            while 1:
                if nei[u]<0:
                    if nei[u]<=start: res=max(res,nei[u]-pos)
                    break
                v=nei[u]
                nei[u]=pos
                pos-=1
                u=v
        return res
        



