# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:

#         g=defaultdict(list)
#         n=len(tickets)
#         tickets.sort()
#         for f,t in tickets:
#             g[f].append(t)
        
#         def dfs(u):
#             if len(res)==n+1: return True
#             for i,v in enumerate(g[u]):
#                     g[u].pop(i)
#                     res.append(v)
#                     if dfs(v): return True
#                     res.pop()
#                     g[u].insert(i,v)
#             return False
        
#         res=["JFK"]
#         dfs("JFK")
#         return res

# class Solution:

#     def findItinerary(self, tickets):
#         g = collections.defaultdict(list)
#         for a, b in sorted(tickets,reverse=True):
#             g[a].append(b)
#         res = []
#         def dfs(u):
#             while g[u]:
#                 dfs(g[u].pop())
#             res.append(u)
#         dfs('JFK')
#         return res[::-1]

# class Solution:

#     def findItinerary(self, tickets):
#         g = collections.defaultdict(list)
#         for a, b in sorted(tickets):
#             g[a].append(b)
#         res = []
#         def dfs(u):
#             while g[u]:
#                 dfs(g[u].pop(0))
#             res.append(u)
#         dfs('JFK')
#         return res[::-1]



class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Observation:
        #     Though we choose a node with smallest lexical order, it could be a dead end
        #     Important Observation is "You may assume all tickets form at least one valid itinerary"
        #     If we have multiple paths from a node, then we can have atmost 1 path which is a dead end

        #             D
        #            | |
        #         B - A = C

        tickets.sort(reverse=True)
        g=defaultdict(list)
        for u,v in tickets:
            g[u].append(v)
        
        def dfs(u):
            while g[u]: dfs(g[u].pop())
            res.append(u)

        res=[]
        dfs("JFK")
        
        return res[::-1]

# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:

#         # Observation:
#         #     Though we choose a node with smallest lexical order, it could be a dead end
#         #     Important Observation is "You may assume all tickets form at least one valid itinerary"
#         #     If we have multiple paths from a node, then we can have atmost 1 path which is a dead end

#         #             D
#         #            | |
#         #         B - A = C

#         tickets.sort()
#         g=defaultdict(deque)
#         for u,v in tickets:
#             g[u].append(v)

#         res,st=[],["JFK"]
#         while st:
#             curr=st[-1]
#             if g[curr]: st.append(g[curr].popleft())
#             else: res.append(st.pop())
        
#         return res[::-1]
                