# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:

#         @cache
#         def dfs(k: int, r1: int, r2: int):

#             if r1 < 0 or r2 < 0 or r1 > r2: return -1

#             c1,c2 = k-r1,k-r2

#             if c1 < 0 or c2 < 0 or grid[r1][c1] < 0 or grid[r2][c2] < 0: return -1

#             if k==0: return grid[0][0]

#             prev = max(
#                 dfs(k-1, r1, r2),
#                 dfs(k-1, r1-1, r2),
#                 dfs(k-1, r1, r2-1),
#                 dfs(k-1, r1-1, r2-1)
#             )
#             if prev==-1: return -1

#             if r1 == r2: return prev + grid[r1][c1]
#             return prev + grid[r1][c1] + grid[r2][c2]

#         N = len(grid)
#         return max(dfs(2*N-2, N-1, N-1), 0)


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        @cache
        def helper(r1,c1,r2,c2):
            if r1==n or c1==n or r2==n or c2==n or grid[r1][c1]==-1 or grid[r2][c2]==-1 or r1<r2: return -inf #r1<r2 reduces search by half because they can switch places, leading to 2 times the required search
            if r1==c1==r2==c2==n-1: return grid[n-1][n-1]
            next=max(
                helper(r1,c1+1,r2,c2+1),
                helper(r1+1,c1,r2+1,c2),
                helper(r1+1,c1,r2,c2+1),
                helper(r1,c1+1,r2+1,c2)
            )

            if r1==r2 and c1==c2: return grid[r1][c2]+next
            return grid[r1][c1]+grid[r2][c2]+next
        return max(helper(0,0,0,0),0)
