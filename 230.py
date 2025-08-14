# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

#         cnt=[0]
#         res=[-1]
#         def inorder(node):
#             if not node: return
#             inorder(node.left)
#             cnt[0]+=1
#             if cnt[0]==k: res[0]=node.val
#             inorder(node.right)

#         inorder(root)
#         return res[0]

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

#         cnt=[0]
#         def inorder(node):
#             if not node: return None
#             res=inorder(node.left)
#             if res!=None: return res
#             cnt[0]+=1
#             if cnt[0]==k: return node.val
#             res=inorder(node.right)
#             return res
        
#         return inorder(root)

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

#         st=[]
#         node=root
#         while node:
#             st.append(node)
#             node=node.left
        
#         while st:
#             node=st.pop()
#             k-=1
#             if k==0: return node.val
#             node=node.right
#             while node:
#                 st.append(node)
#                 node=node.left

#         return -1

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        st=[]
        node=root
        while st or node:
            if node:
                st.append(node)
                node=node.left
            else:
                node=st.pop()
                k-=1
                if k==0: return node.val
                node=node.right
                
        return -1

# # for the followup create this data structure
# def kthSmallestRecur(root, k):
#     if root is None:
#         return -1

#     # Search left subtree
#     if k[0] < root.lCount + 1:
#         return kthSmallestRecur(root.left, k)
    
#     # return curr node 
#     elif k[0] == root.lCount + 1:
#         return root.data
    
#     # decrement k by (lCount+1) and 
#     # search right subtree
#     else:
#         k[0] -= (root.lCount + 1)
#         return kthSmallestRecur(root.right, k)

# # Function to find kth smallest value in BST.
# def kthSmallest(root, k):
#     kRef = [k]
#     return kthSmallestRecur(root, kRef)


        