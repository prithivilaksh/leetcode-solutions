# class Solution:
#     def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

#         infects=defaultdict(list)
#         n=len(graph)
#         def bfs(u,mal):
#             q=deque([u])
#             while q:
#                 u=q.popleft()
#                 infects[u].append(mal)
#                 for v in range(n):
#                     if graph[u][v] and v not in vis:
#                         vis.add(v)
#                         q.append(v)

#         for u in initial:
#             vis=set(initial)
#             bfs(u,u)
        
#         res=[0]*n
#         for u in infects:
#             if len(infects[u])==1:
#                 res[infects[u][0]]+=1
        
#         return res.index(max(res))

# class Solution:
#     def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

#         infects=defaultdict(list)
#         n=len(graph)
#         def dfs(u,mal):
#             infects[u].append(mal)
#             vis.add(u)
#             for v in range(n):
#                 if graph[u][v] and v not in vis:
#                     dfs(v,mal)

#         for u in initial:
#             vis=set(initial)
#             dfs(u,u)
        
#         res=[0]*n
#         for u in infects:
#             if len(infects[u])==1:
#                 res[infects[u][0]]+=1
        
#         return res.index(max(res))


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        n=len(graph)
        bcnt,bind=1000,0
        for i in sorted(initial):
            vis=set(initial)
            # q=deque([x for x in initial if x!=i])
            q=deque(filter(lambda x:x!=i,initial))
            while q:
                u=q.popleft()
                for v in range(n):
                    if graph[u][v] and v not in vis:
                        vis.add(v)
                        q.append(v)
            cnt=len(vis)
            if cnt<bcnt:
                bcnt,bind=cnt,i

        return bind