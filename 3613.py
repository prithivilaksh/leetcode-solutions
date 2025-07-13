class Solution(object):
    def minCost(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """

        edges.sort(key=lambda x: x[2])
        par=[i for i in range(n)]

        def union(u,v):
            u,v=find(u),find(v)
            par[v]=u
            return u==v

        def find(x):
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]

        comp=n
        if comp<=k: return 0
        for u,v,w in edges:
            isSame=union(u,v)
            if not isSame:
                comp-=1
                if comp<=k: return w   
            
        return -1
