# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res=[-inf]

        def helper(node):
            if not node: return -inf # or 0
            lsum=helper(node.left)
            rsum=helper(node.right)
            csum=max(node.val,lsum+node.val,rsum+node.val)
            res[0]=max(res[0],csum,lsum+node.val+rsum)
            return csum
        
        helper(root)
        return res[0]