class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g=defaultdict(list)
        color=defaultdict(lambda : -1)
        for u,v in dislikes: 
            g[u].append(v)
            g[v].append(u)
        
        def isbipartite(u,c):
            color[u]=c
            for v in g[u]:
                if color[v]==c : return False
                elif color[v]==-1 and not isbipartite(v,c^1): return False
            return True
        
        for u in range(1,n+1):
            if color[u]==-1 and not isbipartite(u,0): return False
        
        return True
        
        
