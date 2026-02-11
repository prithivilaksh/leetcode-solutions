class Solution:
    def minReorder(self, n: int, conn: List[List[int]]) -> int:
        g=defaultdict(list)
        for u,v in conn:
            g[u].append((v,1))
            g[v].append((u,0))
            
        res=[0]
        def dfs(u,p):
            for v,c in g[u]:
                if v!=p:
                    res[0]+=c
                    dfs(v,u)
        dfs(0,-1)
        return res[0]