from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        dq=deque()
        def inorder(node):
            if not node: return
            inorder(node.left)
            dq.append(node.val)
            if len(dq)>k:
                if abs(dq[0]-target)>abs(dq[-1]-target): dq.popleft()
                else: dq.pop()
            inorder(node.right)
        
        inorder(root)
        return list(dq)

if __name__=="__main__":
    root=TreeNode(4)
    root.left=TreeNode(2)
    root.right=TreeNode(5)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(3)
    target=3.714286
    k=2
    print(Solution().closestKValues(root,target,k))
# Input: root = [4,2,5,1,3], target = 3.714286, k = 2
# Output: [4,3]

    
        
        