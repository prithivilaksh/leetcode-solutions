class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        
        g,p=defaultdict(list),defaultdict(set)
        
        for u,v in edges: g[u].append(v);g[v].append(u)
        for u,v in guesses: p[v].add(u)

        def dfs1(u,b):
            for v in g[u]:
                if v!=b:
                    cnt[0]+= u in p[v]
                    dfs1(v,u)
        
        def dfs2(u,b):
            for v in g[u]:
                if v!=b:
                    cnt[v]=cnt[u] - (u in p[v]) + (v in p[u])
                    dfs2(v,u)
        
        n=len(edges)+1
        cnt=[0]*n
        dfs1(0,-1)
        dfs2(0,-1)
        return sum(1 for c in cnt if c>=k)
            