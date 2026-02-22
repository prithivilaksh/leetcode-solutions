# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
#         g=defaultdict(list)
#         def dfs(root):
#             if not root: return
#             left,right=root.left,root.right
#             if left:
#                 g[root.val].append(left.val)
#                 g[left.val].append(root.val)
#                 dfs(left)
#             if right:
#                 g[root.val].append(right.val)
#                 g[right.val].append(root.val)
#                 dfs(right)
        
#         dfs(root)
#         dq,vis=deque([target.val]),set([target.val])
#         for _ in range(k):
#             for _ in range(len(dq)):
#                 u=dq.popleft()
#                 for v in g[u]:
#                     if v not in vis:
#                         vis.add(v)
#                         dq.append(v)

#         return list(dq)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        p=defaultdict(lambda : None)
        dq=deque([root])
        
        while dq:
            u=dq.popleft()
            for v in (u.left,u.right):
                if not v: continue
                p[v]=u
                dq.append(v)

        dq,vis=deque([target]),set([target,None])
        for _ in range(k):
            for _ in range(len(dq)):
                u=dq.popleft()
                for v in (u.left,u.right,p[u]):
                    if v in vis: continue
                    vis.add(v)
                    dq.append(v)

        return [u.val for u in dq]
