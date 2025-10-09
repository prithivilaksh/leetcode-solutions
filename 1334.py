# class Solution:
#     def findTheCity(self, n: int, edges: List[List[int]], t: int) -> int:
        
#         d=[[inf]*n for _ in range(n)]
#         for i in range(n): d[i][i]=0
#         for u,v,w in edges: d[u][v]=d[v][u]=w

#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     if d[i][k]==inf or d[k][j]==inf: continue
#                     d[i][j]=min(d[i][j],d[i][k]+d[k][j])
        
#         mi,res=inf,-1
#         for i in range(n):
#             cnt=0
#             for j in range(n):
#                 if d[i][j]<=t: cnt+=1
#             if cnt<=mi: mi,res=cnt,i
#         return res

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], t: int) -> int:
        
        g=defaultdict(list)
        for u,v,w in edges: 
            g[u].append((v,w))
            g[v].append((u,w))
        
        def djikstra(u):
            h=[(0,u)]
            dis=[inf]*n
            dis[u]=cnt=0
            while h:
                d,u=heappop(h)
                if d>dis[u]: continue
                cnt+=1
                for v,dv in g[u]:
                    if d+dv<dis[v] and d+dv<=t:
                        dis[v]=d+dv
                        heappush(h,(dis[v],v))
            return cnt
        
        mi,res=inf,-1
        for i in range(n):
            cnt=djikstra(i)
            if cnt<=mi: mi,res=cnt,i
        return res