
# class Solution:
#     def processQueries(self, c: int, conn: List[List[int]], qs: List[List[int]]) -> List[int]:


#         g=defaultdict(list)
#         comp=defaultdict(list)
#         par=[-1 for i in range(c+1)]
#         on=[True for i in range(c+1)]
        
#         for [u,v] in conn:
#             g[u].append(v)
#             g[v].append(u)
        

#         def dfs(u,mi):
#             par[u]=mi
#             heappush(comp[mi],u)
#             for v in g[u]:
#                 if par[v]==-1:
#                     dfs(v,mi)
        
#         for u in range(1,c):
#             if par[u]==-1:
#                 dfs(u,u)

#         res=[]
#         for [tp,u] in qs:
#             if tp==1: 
#                 if on[u]: res.append(u)
#                 else: 
#                     mi=par[u]
#                     # heapify(comp[mi])
#                     while comp[mi]:
#                         if on[comp[mi][0]]==False:
#                             heappop(comp[mi])
#                         else: 
#                             res.append(comp[mi][0])
#                             break
                        
#                     if not comp[mi]: res.append(-1)
#             else:
#                 on[u]=False

#         return res
            
                
# class Solution:
#     def processQueries(self, c: int, conn: List[List[int]], qs: List[List[int]]) -> List[int]:

#         g=defaultdict(list)
#         comp=defaultdict(list)
#         par=[-1 for i in range(c+1)]
#         on=[True for i in range(c+1)]
        
#         for [u,v] in conn:
#             g[u].append(v)
#             g[v].append(u)
        

#         def dfs(u,mi):
#             par[u]=mi
#             heappush(comp[mi],u)
#             for v in g[u]:
#                 if par[v]==-1: dfs(v,mi)
        
#         for u in range(1,c):
#             if par[u]==-1: dfs(u,u)

#         res=[]
#         for [tp,u] in qs:
#             if tp==1: 
#                 if on[u]: res.append(u)
#                 else: 
#                     mi=par[u]
#                     while comp[mi] and not on[comp[mi][0]]: heappop(comp[mi])
#                     res.append(comp[mi][0] if comp[mi] else -1)
#             else: on[u]=False

#         return res


# class Solution:
#     def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
#         G = [[] for _ in range(c + 1)]
#         for u, v in connections:
#             G[u].append(v)
#             G[v].append(u)

#         seen = [0] * (c + 1)
#         def dfs(i, v):
#             if seen[i]: return
#             seen[i] = v
#             for j in G[i]:
#                 dfs(j, v)
#             return

#         for i in range(1, c + 1):
#             dfs(i, i)

#         todo = defaultdict(list)
#         for i in range(c, 0, -1):
#             todo[seen[i]].append(i)
#         res = []
#         online = [1] * (c + 1)
#         for o, x in queries:
#             if o == 1:
#                 if online[x]:
#                     res.append(x)
#                     continue
#                 y = seen[x]
#                 while todo[y] and online[todo[y][-1]] == 0:
#                     todo[y].pop()
#                 res.append(todo[y][-1] if todo[y] else -1)
#             if o == 2:
#                 online[x] = 0
#         return res

# class Solution:
#     def processQueries(self, c: int, conn: List[List[int]], qs: List[List[int]]) -> List[int]:

#         par=[i for i in range(c+1)]
#         on=[True] * (c+1)
#         comppq=defaultdict(list)
#         res=[]

#         def union(a,b):
#             a,b=find(a),find(b)
#             par[b]=a
        
#         def find(x):
#             if x==par[x]: return x
#             par[x]=find(par[x])
#             return par[x]
        
#         for u,v in conn: union(u,v)
        
#         for u in range(1,c+1): heappush(comppq[find(u)],u)
        
#         for tp,u in qs:
#             if tp==2: on[u]=False
#             elif on[u]: res.append(u)
#             else:
#                 pq=comppq[find(u)]
#                 while pq and not on[pq[0]]: heappop(pq)
#                 res.append(pq[0] if pq else -1)
        
#         return res

class Solution:
    def processQueries(self, c: int, conn: List[List[int]], qs: List[List[int]]) -> List[int]:

        g=defaultdict(list)
        comp=defaultdict(list)
        par=[-1]*(c+1)
        on=[True]*(c+1)
        
        for [u,v] in conn:
            g[u].append(v)
            g[v].append(u)
        

        def dfs(u,mi):
            par[u]=mi
            for v in g[u]:
                if par[v]==-1: dfs(v,mi)
        
        for u in range(1,c+1):
            if par[u]==-1: dfs(u,u)
            mi=par[u]
            comp[mi].append(u)     

        for vs in comp.values(): vs.reverse()       

        res=[]
        for tp,u in qs:
            if tp==2: on[u]=False
            elif on[u]: res.append(u)
            else:
                mi=par[u]
                while comp[mi] and not on[comp[mi][-1]]: comp[mi].pop()
                res.append(comp[mi][-1] if comp[mi] else -1)

        return res

        
                
                

        