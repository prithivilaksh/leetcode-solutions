"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
#         mp=defaultdict(lambda : Node())

#         def dfs(u):
#             if not u: return None
#             val=u.val
#             if val in mp: return mp[val]
#             mp[val].val=val
#             for v in u.neighbors:
#                 mp[val].neighbors.append(dfs(v))
#             return mp[val]
        
#         return dfs(node)

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
#         if not node: return None

#         mp=defaultdict(lambda: Node())

#         q=[node]
#         mp[node.val].val=node.val

#         while q:
#             u=q.pop()
#             nu=mp[u.val]
#             for v in u.neighbors:
#                 if v.val not in mp:
#                     mp[v.val].val=v.val
#                     q.append(v)
#                 nu.neighbors.append(mp[v.val])
        
#         return mp[node.val]


# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
#         if not node: return None

#         mp=defaultdict(lambda: Node())

#         q=[node]
#         mp[node].val=node.val

#         while q:
#             u=q.pop()
#             for v in u.neighbors:
#                 if v not in mp:
#                     mp[v].val=v.val
#                     q.append(v)
#                 mp[u].neighbors.append(mp[v])
        
#         return mp[node]

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: return None

        mp={node:Node(node.val)}
        q=deque([node])

        while q:
            u=q.popleft()
            for v in u.neighbors:
                if v not in mp:
                    mp[v]=Node(v.val)
                    q.append(v)
                mp[u].neighbors.append(mp[v])
        
        return mp[node]
        

                
    