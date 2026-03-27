class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        g=defaultdict(list)
        for u,v,p in flights: g[u].append((v,p))

        stops=[inf]*n
        stops[src]=0
        h=[(0,0,src)]

        while h:
            cp,s,u=heappop(h)
            if stops[u]<s: continue
            if u==dst: return cp
            stops[u]=s
            for v,p in g[u]:
                if s+1<stops[v] and s+1<=k+1:
                    heappush(h,(cp+p,s+1,v))

        return -1