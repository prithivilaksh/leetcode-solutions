# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
#         @cache
#         def dp(l,r):
#             if l>r: return [None]
#             if l==r: return [TreeNode(l)]
#             res=[]
#             for m in range(l,r+1):
#                 for left in dp(l,m-1):
#                     for right in dp(m+1,r):
#                         res.append(TreeNode(m,left,right))
#             return res
#         return dp(1,n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def dp(l,r):
            res=[]
            for m in range(l,r+1):
                for left in dp(l,m-1):
                    for right in dp(m+1,r):
                        res.append(TreeNode(m,left,right))
            return res or [None]
        return dp(1,n)