# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []

#         def dfs(node, depth):
#             if not node:
#                 return None
#             if len(res) == depth:
#                 res.append([])

#             res[depth].append(node.val)
#             dfs(node.left, depth + 1)
#             dfs(node.right, depth + 1)

#         dfs(root, 0)
#         return res

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        if not root: return []
        q,res=deque([root]),[]
        while q:
            l=len(q)
            ires=[]
            for _ in range(l):
                c=q.popleft()
                ires.append(c.val)
                if c.left: q.append(c.left)
                if c.right: q.append(c.right)
            res.append(ires)
        return res