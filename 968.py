# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return 0
            l=dfs(root.left)
            r=dfs(root.right)

            if l==2 or r==2: res[0]+=1;return 1
            if l==1 or r==1: return 0
            if l==0 and r==0: return 2
            
        res=[0]
        if dfs(root)==2: res[0]+=1
        return res[0]