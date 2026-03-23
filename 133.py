# # """
# # # Definition for a Node.
# # class Node:
# #     def __init__(self, val = 0, neighbors = None):
# #         self.val = val
# #         self.neighbors = neighbors if neighbors is not None else []
# # """

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node: return None
#         mp,vis={},set()

#         def getnewnode(x):
#             if x not in mp: mp[x]=Node(x.val)
#             return mp[x]

#         def dfs(u):
#             vis.add(u)
#             nu=getnewnode(u)
#             for v in u.neighbors:
#                 nv=getnewnode(v)
#                 nu.neighbors.append(nv)
#                 if v not in vis: dfs(v)
        
#         dfs(node)
#         return mp[node]


# # """
# # # Definition for a Node.
# # class Node:
# #     def __init__(self, val = 0, neighbors = None):
# #         self.val = val
# #         self.neighbors = neighbors if neighbors is not None else []
# # """

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
#         if not node: return None

#         mp={node:Node(node.val)}
#         dq=deque([node])
#         while dq:
#             u=dq.popleft()
#             for v in u.neighbors:
#                 if v not in mp: 
#                     mp[v]=Node(v.val)
#                     dq.append(v)
#                 mp[u].neighbors.append(mp[v])

#         return mp[node]


# # """
# # # Definition for a Node.
# # class Node:
# #     def __init__(self, val = 0, neighbors = None):
# #         self.val = val
# #         self.neighbors = neighbors if neighbors is not None else []
# # """

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        mp={}
        def dfs(u):
            mp[u]=Node(u.val)
            for v in u.neighbors:
                if v not in mp: dfs(v)
                mp[u].neighbors.append(mp[v])
        
        dfs(node)
        return mp[node]
