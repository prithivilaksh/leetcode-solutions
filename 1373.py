# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
#         res=[0]
#         def helper(node):
#             if not node: return None,0,True,None

#             lmin,lsum,lbst,lmax=helper(node.left)
#             rmin,rsum,rbst,rmax=helper(node.right)

#             if lbst and rbst:
#                 isBst=True
#                 if lmax and rmin: isBst=lmax<node.val<rmin
#                 elif lmax: isBst=lmax<node.val
#                 elif rmin: isBst=node.val<rmin

#                 if isBst: 
#                     cmin=cmax=node.val
#                     if rmax: cmax=max(cmax,rmax)
#                     if lmin: cmin=min(cmin,lmin)
#                     csum=lsum+node.val+rsum
#                     res[0]=max(res[0],csum)
#                     return cmin,csum,isBst,cmax

#             return None,0,False,None
#         helper(root) 
#         return res[0]



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        res=[0]
        def helper(node):
            if not node: return inf,0,-inf

            lmin,lsum,lmax=helper(node.left)
            rmin,rsum,rmax=helper(node.right)

            if lmax<node.val<rmin:
                cmax=max(node.val,rmax)
                cmin=min(node.val,lmin)
                csum=lsum+node.val+rsum
                res[0]=max(res[0],csum)
                return cmin,csum,cmax

            return -inf,0,inf,

        helper(root) 
        return res[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
#         res=[0]
#         def helper(node):

#             lmin,lsum,lmax=helper(node.left) if node.left else (node.val,0,node.val-1)
#             rmin,rsum,rmax=helper(node.right) if node.right else (node.val+1,0,node.val)

#             if lmax<node.val<rmin:
#                 cmax=max(node.val,rmax)
#                 cmin=min(node.val,lmin)
#                 csum=lsum+node.val+rsum
#                 res[0]=max(res[0],csum)
#                 return cmin,csum,cmax

#             return -inf,0,inf,

#         helper(root) 
#         return res[0]
