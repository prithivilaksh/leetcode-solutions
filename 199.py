# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
#         def dfs(node,d):
#             if not node: return
#             if d==len(res): res.append(node.val)
#             dfs(node.right,d+1)
#             dfs(node.left,d+1)
#         res=[]
#         dfs(root,0)
#         return res


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root: return []
#         dq,d,res=deque([root]),0,[]
#         while dq:
#             for _ in range(len(dq)):
#                 node=dq.popleft()
#                 if d==len(res): res.append(node.val)
#                 if node.right: dq.append(node.right)
#                 if node.left: dq.append(node.left)
#             d+=1
#         return res
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        dq,d,res=deque([root]),0,[]
        while dq:
            l=len(dq)
            for i in range(l):
                node=dq.popleft()
                if i==l-1: res.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            d+=1
        return res
        