# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node: return 0
            lcnt=dfs(node.left)
            rcnt=dfs(node.right)
            res[0]+=abs(lcnt)+abs(rcnt)
            return node.val+lcnt+rcnt-1
            
        res=[0]
        dfs(root)
        return res[0]