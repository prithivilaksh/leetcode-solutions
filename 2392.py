class Solution:
    def buildMatrix(self, k: int, rowCond: List[List[int]], colCond: List[List[int]]) -> List[List[int]]:
        
        def topologicalSort(cond):
            g=defaultdict(list)
            deg=[0]*(k+1)
            for a,b in cond:
                deg[b]+=1
                g[a].append(b)

            dq=deque([u for u in range(1,k+1) if deg[u]==0])
            order=[]
            while dq:
                u=dq.popleft()
                order.append(u)
                for v in g[u]:
                    deg[v]-=1
                    if deg[v]==0: dq.append(v)
            if len(order)!=k: return []
            return {x:i for i,x in enumerate(order)}
        
        if not (order1:=topologicalSort(rowCond)): return []
        if not (order2:=topologicalSort(colCond)): return []
        res=[[0]*k for _ in range(k)]
        for x in range(1,k+1):
            res[order1[x]][order2[x]]=x

        
        return res