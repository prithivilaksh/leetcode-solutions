# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def getDirections(self, root: TreeNode | None, u: int, v: int) -> str:
#         def dfs(node,x):
#             if node:
#                 if node.val==x: return ""
#                 l=dfs(node.left,x)
#                 if l is not None: return "L"+l
#                 r=dfs(node.right,x)
#                 if r is not None: return "R"+r
#             return None
        
#         roottou=dfs(root,u)
#         roottov=dfs(root,v)

#         def remove_common_prefix(a,b):
#             n,i=min(len(a),len(b)),0
#             while i<n and a[i]==b[i]: i+=1
#             return a[i:],b[i:]
        
#         tou,tov=remove_common_prefix(roottou,roottov)
#         return len(tou)*'U'+tov


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, u: int, v: int) -> str:
        def dfs(node,x,acc):
            if node:
                if node.val==x: return True
                if dfs(node.left,x,acc): 
                    acc.append("L")
                    return True
                if dfs(node.right,x,acc): 
                    acc.append("R")
                    return True
            return False
        
        tou,tov=[],[]
        dfs(root,u,tou);dfs(root,v,tov)
        while tou and tov and tou[-1]==tov[-1]: tou.pop();tov.pop()
            
        return len(tou)*'U'+''.join(tov[::-1])
