class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        n=len(edges)+1
        time=[inf]*n
        def bobdfs(u,p,t):
            if u==0: 
                time[u]=t
                return True
            for v in g[u]:
                if v!=p:
                    if bobdfs(v,u,t+1):
                        time[u]=t
                        return True

        def open(u,t):
            if t<time[u]: return amount[u]
            if t==time[u]: return amount[u]//2
            return 0

        def alicedfs(u,p,t):
            cost=open(u,t)
            pl=-inf
            for v in g[u]:
                if v!=p:
                    pl=max(pl,alicedfs(v,u,t+1))
            return cost+pl if pl!=-inf else cost
        
        g=defaultdict(list)
        for u,v in edges: g[u].append(v);g[v].append(u)
        
        bobdfs(bob,-1,0)
        return alicedfs(0,-1,0)