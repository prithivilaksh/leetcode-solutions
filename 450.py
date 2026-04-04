# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

#         def insert(newnode,node):
#             if not node or not newnode: return newnode
#             if newnode.val < node.val: node.left=insert(newnode,node.left)
#             else: node.right=insert(newnode,node.right)
#             return node

#         def delete(node):
#             if not node: return None
#             if key==node.val:
#                 if node.left and node.right:
#                     tobeins=node.left.right
#                     node.left.right=node.right
#                     node.right=insert(tobeins,node.right)
#                     return node.left
#                 elif node.left: return node.left
#                 else: return node.right
#             elif key<node.val: node.left=delete(node.left)
#             else: node.right=delete(node.right)
#             return node
#         return delete(root)
        


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

#         def delete(node):
#             if not node: return None
#             if key<node.val: node.left=delete(node.left)
#             elif key>node.val: node.right=delete(node.right)
#             else:
#                 if not node.left: return node.right
#                 if not node.right: return node.left
#                 newroot=node.left
#                 tobeins=newroot.right
#                 newroot.right=node.right
#                 it=newroot.right
#                 while it.left: it=it.left
#                 it.left=tobeins
#                 return newroot
#             return node
#         return delete(root)
        



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

#         def removeAndGetInOrderSuccessor(node):

#             if node.left: 
#                 node.left,x=removeAndGetInOrderSuccessor(node.left)
#                 return node,x
#             else:
#                 return node.right,node.val

#         def delete(node):
#             if not node: return None
#             if key<node.val: node.left=delete(node.left)
#             elif node.val<key: node.right=delete(node.right)
#             else: 
#                 if not node.left: return node.right
#                 if not node.right: return node.left

#                 node.right,node.val=removeAndGetInOrderSuccessor(node.right)

#             return node
        
#         return delete(root)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

#         def delete(node):
#             if not node: return None
#             if key<node.val: node.left=delete(node.left)
#             elif node.val<key: node.right=delete(node.right)
#             else: 
#                 if not node.left: return node.right
#                 if not node.right: return node.left

#                 newroot=node.left
#                 tobeins=newroot.right
#                 newroot.right=it=node.right
#                 while it.left: it=it.left
#                 it.left=tobeins
#                 return newroot

#             return node
        
#         return delete(root)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(node):
            if not node: return None
            if key<node.val: node.left=delete(node.left)
            elif node.val<key: node.right=delete(node.right)
            else: 
                if not node.left: return node.right
                if not node.right: return node.left
                newroot=it=node.left
                tobeins=node.right
                while it.right: it=it.right
                it.right=tobeins
                return newroot

            return node
        
        return delete(root)















        