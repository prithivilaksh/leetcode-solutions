"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

# class Solution:
#     def construct(self, grid: List[List[int]]) -> 'Node':
        
#         n=len(grid)
#         if n==1: return Node(grid[0][0],True,None,None,None,None)
#         m=n//2

#         tl=self.construct([row[:m] for row in grid[:m]])
#         tr=self.construct([row[m:] for row in grid[:m]])
#         bl=self.construct([row[:m] for row in grid[m:]])
#         br=self.construct([row[m:] for row in grid[m:]])
#         if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val==tr.val==bl.val==br.val:
#             return Node(tl.val,True,None,None,None,None)
#         return Node(0,False,tl,tr,bl,br)

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
                        break
            if all_same: return Node(grid[r][c], True)
            
            n = n // 2
            tl = dfs(n, r, c)
            tr = dfs(n, r, c + n)
            bl = dfs(n, r + n, c)
            br = dfs(n, r + n, c + n)
            return Node(0, False, tl, tr, bl, br)
        return dfs(len(grid), 0, 0)