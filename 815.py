# TLE
# class Solution:
#     def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
#         routes=[set(r) for r in routes]
#         stops2routes=defaultdict(list)

#         for i,r in enumerate(routes):
#             for stop in r:
#                 stops2routes[stop].append(i)
        
#         dq=deque([source])
#         vis=set([source])
#         d=0
#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==target: return d
#                 for i in stops2routes[u]:
#                     for v in routes[i]:
#                         if v not in vis:
#                             vis.add(v)
#                             dq.append(v)
#             d+=1

#         return -1

# class Solution:
#     def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
#         routes=[set(r) for r in routes]
#         stops2routes=defaultdict(list)

#         for i,r in enumerate(routes):
#             for stop in r:
#                 stops2routes[stop].append(i)
        
#         dq=deque([source])
#         vis=set([source])
#         d=0
#         while dq:
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 if u==target: return d
#                 while stops2routes[u]:
#                     i=stops2routes[u].pop()
#                     while routes[i]:
#                         v=routes[i].pop()
#                         if v not in vis:
#                             vis.add(v)
#                             dq.append(v)
#             d+=1

#         return -1


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source==target: return 0

        routes=[set(r) for r in routes]
        stops2routes=defaultdict(list)

        for i,r in enumerate(routes):
            for stop in r:
                stops2routes[stop].append(i)
                
        if source not in stops2routes or target not in stops2routes: return -1

        dq=deque([source])
        d=0
        while dq:
            for _ in range(len(dq)):
                u=dq.popleft()
                if u==target: return d
                while stops2routes[u]:
                    i=stops2routes[u].pop()
                    while routes[i]:
                        v=routes[i].pop()
                        dq.append(v)
            d+=1

        return -1
                