# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None
# """

# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
#         def helper(node):
#             if node.val in st: return node
#             st.add(node.val)
#             if node.parent: return helper(node.parent)
        
#         st=set()
#         helper(p)
#         return helper(q)

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
#         st=set()
#         while p:
#             st.add(p.val)
#             p=p.parent
        
#         while q:
#             if q.val in st: return q
#             q=q.parent


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr1, ptr2 = p, q
        while ptr1 != ptr2:
            ptr1 = ptr1.parent if ptr1.parent else q
            ptr2 = ptr2.parent if ptr2.parent else p
        return ptr1