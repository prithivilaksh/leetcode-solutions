# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         def dfs(root):
#             if not root: return inf,-inf,True
#             lmi,lmx,lbtree=dfs(root.left)
#             rmi,rmx,rbtree=dfs(root.right)
#             if lbtree and rbtree:
#                 if lmx<root.val and root.val<rmi:
#                     return min(lmi,root.val),max(root.val,rmx),True

#             return None,None,False
        
#         return dfs(root)[2]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(lpar,root,rpar):
            if not root: return True
            if lpar>=root.val or root.val>=rpar: return False
            return dfs(lpar,root.left,root.val) and dfs(root.val,root.right,rpar)
        
        return dfs(-inf,root,inf)
