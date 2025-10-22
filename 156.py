# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # The original left child becomes the new root.
        # The original root becomes the new right child.
        # The original right child becomes the new left child.

        # The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.

        if not root: return root

        def helper(root):
            if not root.left: return root
            new_root=helper(root.left)

            root.left.left=root.right
            root.left.right=root
            root.left=root.right=None
            
            return new_root


        return helper(root)