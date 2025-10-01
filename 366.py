from typing import Optional, List

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node: Optional[TreeNode]) -> int:
            if not node : return -1
            ht = max(dfs(node.left), dfs(node.right)) + 1
            if len(res) == ht: res.append([])
            res[ht].append(node.val)
            return ht

        res = []
        dfs(root)
        return res