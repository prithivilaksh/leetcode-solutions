# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res=[]
#         def preorder(root):
#             if not root: return
#             res.append(root.val)
#             preorder(root.left)
#             preorder(root.right)
#         preorder(root)
#         return res

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        st=[]
        node=root
        while st or node:
            if node:
                res.append(node.val)
                st.append(node)
                node=node.left
            else:
                node=st.pop()
                node=node.right
        return res
        