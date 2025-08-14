# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res=[]
#         def postorder(root):
#             if not root: return
#             postorder(root.left)
#             postorder(root.right)
#             res.append(root.val)
#         postorder(root)
#         return res   

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        node=root
        st=[]

        while node or st:
            if node:
                res.append(node.val)
                st.append(node)
                node=node.right
            else:
                node=st.pop()
                node=node.left

        return res[::-1]