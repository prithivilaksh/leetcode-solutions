# class Solution:
#     def criticalConnections(self, n: int, conns: List[List[int]]) -> List[List[int]]:
        
#         g=defaultdict(list)
#         for u,v in conns:
#             g[u].append(v)
#             g[v].append(u)
        
#         low=[n]*n
#         res=[]

#         def dfs(par,cur,time):
#             low[cur]=time
#             for nei in g[cur]:
#                 if nei==par: continue
#                 if low[nei]==n: 
#                     dfs(cur,nei,time+1)
#                     if time+1==low[nei]: res.append([cur,nei])
#                 low[cur]=min(low[cur],low[nei])
                
#         dfs(-1,0,0)
        
#         return res


# class Solution:
#     def criticalConnections(self, n: int, conns: List[List[int]]) -> List[List[int]]:
#         g = defaultdict(list)
#         for u,v in conns:
#             g[u].append(v)
#             g[v].append(u)
        
#         low,time,res = [n]*n,[0],[]
#         def dfs(par,u):
#             ctime = low[u] = time[0]
#             time[0]+=1
#             for v in g[u]:
#                 if v==par:continue
#                 if low[v]==n:
#                     dfs(u,v)
#                     if ctime<low[v]:res.append([u,v])
#                 low[u] = min(low[u],low[v])
        
#         dfs(-1,0)
#         return res


class Solution:
    def criticalConnections(self, n: int, conns: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for u,v in conns:
            g[u].append(v)
            g[v].append(u)
        
        dis,low,time,res = [n]*n,[n]*n,[0],[]

        def dfs(par,u):

            dis[u]=low[u]=time[0]
            time[0]+=1

            for v in g[u]:
                if v==par: continue
                if dis[v]==n:
                    dfs(u,v)
                    low[u]=min(low[u],low[v])
                    if dis[u]<low[v]: res.append([u,v])
                else: low[u]=min(low[u],dis[v])
        
        dfs(-1,0)
        return res
