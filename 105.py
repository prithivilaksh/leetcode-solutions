# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
        
#         if len(pre)==0: return None

#         root=TreeNode(pre[0])
#         i=ino.index(root.val)
        
#         root.left=self.buildTree(pre[1:i+1],ino[:i])
#         root.right=self.buildTree(pre[i+1:],ino[i+1:])

#         return root
        
        
        
class Solution:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
        
        #pre order -> root left right
        #in order  -> left root right
        inoi={x:i for i,x in enumerate(ino)}
        self.p=0
        def helper(l,r):
            if l>r: return None
            root=TreeNode(pre[self.p])
            self.p+=1

            m=inoi[root.val]            
            root.left=helper(l,m-1)
            root.right=helper(m+1,r)
            return root

        return helper(0,len(ino)-1)
        
        
        
