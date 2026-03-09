# class Solution:
#     def findAllPeople(self, n: int, meetings: List[List[int]], fp: int) -> List[int]:
        

#         res=set([0,fp])
#         meetings.sort(key=lambda x:x[2])

#         def helper():
#             vis=set()
#             def dfs(u):
#                 vis.add(u)
#                 for v in g[u]:
#                     if v not in vis:
#                         dfs(v)
#             for u in g.keys():
#                 if u in res and u not in vis: dfs(u)
#             res.update(vis)


#         prevt=0
#         g=defaultdict(set)
#         for i,(u,v,t) in enumerate(meetings):
#             if prevt!=t: 
#                 helper()
#                 g.clear()
#             prevt=t
#             g[u].add(v)
#             g[v].add(u)
#         helper()
#         return list(res)


# class Solution:
#     def findAllPeople(self, n: int, meetings: List[List[int]], fp: int) -> List[int]:
        

#         res=set([0,fp])
#         meetings.sort(key=lambda x:x[2])

#         def helper():
#             def dfs(u):
#                 st=[u]
#                 while st:
#                     u=st[-1]
#                     if g[u]: st.append(g[u].pop())
#                     else: res.add(st.pop())

#             for u in g:
#                 if u in res:
#                     dfs(u)


#         prevt=0
#         g=defaultdict(set)
#         for i,(u,v,t) in enumerate(meetings):
#             if prevt!=t: 
#                 helper()
#                 g.clear()
#             prevt=t
#             if v in res: res.add(u)
#             elif u in res: res.add(v)
#             else:
#                 g[u].add(v)
#                 g[v].add(u)
#         helper()
#         return list(res)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]): 
            g = defaultdict(list)
            for u, v, _ in grp: 
                g[u].append(v)
                g[v].append(u)
       
            dq = deque([u for u in g if u in can])
            while dq: 
                u = dq.popleft()
                for v in g[u]: 
                    if v not in can: 
                        can.add(v)
                        dq.append(v)
        return list(can)