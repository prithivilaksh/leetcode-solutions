# Definition for a binary tree node.
from math import inf
from collections import defaultdict,deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:

        # idea/observation: 
        # 1) at every node, find the distance to the closest leaf and its value
        # 2) if k is found, then return the distance to k from its parent
        res=[inf,None]
        def dfs(node):
            dis,val,kdis=inf,None,inf
            if node.val==k: kdis=0
            if not node.left and not node.right: dis,val=0,node.val
            else:
                if node.left:
                    d,v,kd=dfs(node.left)
                    if d+1<dis: dis,val=d+1,v
                    if kd+1<kdis: kdis=kd+1

                if node.right:
                    d,v,kd=dfs(node.right)
                    if d+1<dis: dis,val=d+1,v
                    if kd+1<kdis: kdis=kd+1

            if kdis+dis<res[0]: res[0],res[1]=kdis+dis,val
            return dis,val,kdis
        dfs(root)
        return res[1]


        

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def dfs(root, p):
            if root:
                g[root].append(p)
                g[p].append(root)
                dfs(root.left, root)
                dfs(root.right, root)

        g = defaultdict(list)
        dfs(root, None)
        q = deque([node for node in g if node and node.val == k])
        seen = set()
        while q:
            node = q.popleft()
            seen.add(node)
            if node:
                if node.left is None and node.right is None:
                    return node.val
                for next in g[node]:
                    if next not in seen:
                        q.append(next)


# Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Output: 3

if __name__=="__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(4)
    root.left.left.left=TreeNode(5)
    root.left.left.left.left=TreeNode(6)
    root.right=TreeNode(3)
    print(Solution().findClosestLeaf(root,2))       