# class Solution:
#     def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        
#         n=len(coins)
#         g=defaultdict(set)
#         indeg=defaultdict(int)

#         for a,b in edges:
#             g[a].add(b)
#             g[b].add(a)
#             indeg[a]+=1
#             indeg[b]+=1
        
#         dq=deque()

#         for i in range(n):
#             if coins[i]==0 and indeg[i]==1:
#                 dq.append(i)

#         while dq:
#             u=dq.popleft()
#             if indeg[u]==0: continue
#             indeg[u]-=1
#             for v in g[u]:
#                 indeg[v]-=1
#                 g[v].remove(u)
#                 if coins[v]==0 and indeg[v]==1:
#                     dq.append(v)
        
#         for i in range(n):
#             if coins[i]==1 and indeg[i]==1:
#                 dq.append(i)
        
#         for _ in range(2):
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if indeg[u]==0: continue
#                 indeg[u]-=1
#                 for v in g[u]:
#                     indeg[v]-=1
#                     g[v].remove(u)
#                     if indeg[v]==1:
#                         dq.append(v)

#         return sum(indeg.values())

        
        

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        
        n=len(coins)
        g=defaultdict(set)

        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
        
        dq=deque()

        for i in range(n):
            if coins[i]==0 and len(g[i])==1:
                dq.append(i)

        while dq:
            u=dq.popleft()
            while g[u]:
                v=g[u].pop()
                g[v].remove(u)
                if coins[v]==0 and len(g[v])==1:
                    dq.append(v)
        
        for i in range(n):
            if coins[i]==1 and len(g[i])==1:
                dq.append(i)
        
        for _ in range(2):
            for _ in range(len(dq)):
                u=dq.popleft()
                while g[u]:
                    v=g[u].pop()
                    g[v].remove(u)
                    if len(g[v])==1:
                        dq.append(v)

        return sum(len(i) for i in g.values())

        
        

