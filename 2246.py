# class Solution:
#     def longestPath(self, par: List[int], s: str) -> int:
        
#         chi,res=defaultdict(list),[0]
#         for i,p in enumerate(par): chi[p].append(i)

#         def dfs(u):
#             first=second=1
#             for v in chi[u]:
#                 l=dfs(v)+1
#                 if s[u]==s[v]: continue
#                 if l>first: first,second=l,first
#                 elif l>second: second=l
#             res[0]=max(res[0],first+second-1)
#             return first
#         dfs(0)
#         return res[0]

class Solution:
    def longestPath(self, par: List[int], s: str) -> int:
        
        n,res=len(par),1
        indeg,h=[0]*n,[1]*n

        for p in par[1:]: indeg[p]+=1
        dq=deque(i for i in range(n) if indeg[i]==0)

        while dq[0]:
            u=dq.popleft()
            p=par[u]
            indeg[p]-=1
            if indeg[p]==0: dq.append(p)
            if s[u]==s[p]: continue
            res=max(res,h[p]+h[u])
            h[p]=max(h[p],h[u]+1)
        return res
        


