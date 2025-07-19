class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n=len(online)
        g=defaultdict(list)
        for u,v,w in edges:
            if online[u] and online[v]:
                g[u].append([v,w])

        dis=defaultdict(lambda: inf)
        q=[[-inf,0,0]]
        while q:
            negmi,tot,u=heappop(q)
            mi=-negmi

            if dis[u]<=tot: continue
            dis[u]=tot

            if u==n-1: return mi

            for v,w in g[u]:
                if tot+w<=k:
                    heappush(q,[-min(mi,w),tot+w,v])

        return -1 
        