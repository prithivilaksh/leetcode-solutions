class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        vis=set()
        def dfs(u):
            vis.add(u)
            for v in rooms[u]:
                if v not in vis:
                    dfs(v)
        dfs(0)
        return len(vis)==len(rooms)

# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
#         vis=set()
#         st=[0]
#         while st:
#             u=st.pop()
#             vis.add(u)
#             for v in rooms[u]:
#                 if v not in vis:
#                     st.append(v)
        
#         return len(vis)==len(rooms)