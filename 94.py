# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res=[]
#         def inorder(root):
#             if not root: return
#             inorder(root.left)
#             res.append(root.val)
#             inorder(root.right)
#         inorder(root)
#         return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        st=[]
        node=root
        while st or node:
            if node:
                st.append(node)
                node=node.left
            else:
                node=st.pop()
                res.append(node.val)
                node=node.right
        return res
        