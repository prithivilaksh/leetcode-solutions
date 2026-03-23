# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         n=len(grid)
#         @cache
#         def dp(r1,c1,r2,c2):
#             if r1==n or c1==n  or r2==n or c2==n or grid[r1][c1]==-1 or grid[r2][c2]==-1: return -inf
#             if r1==r2==c1==c2==n-1: return grid[n-1][n-1]
#             res=grid[r1][c1]+grid[r2][c2] if r1!=r2 else grid[r1][c1]
#             return res+max(
#                 dp(r1+1,c1,r2+1,c2),
#                 dp(r1+1,c1,r2,c2+1),
#                 dp(r1,c1+1,r2+1,c2),
#                 dp(r1,c1+1,r2,c2+1)
#             )
#         return max(dp(0,0,0,0),0)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        @cache
        def dp(r1,c1,r2,c2):
            if r1<r2 or r1==n or c1==n  or r2==n or c2==n or grid[r1][c1]==-1 or grid[r2][c2]==-1: return -inf
            if r1==r2==c1==c2==n-1: return grid[n-1][n-1]
            res=grid[r1][c1]+grid[r2][c2] if r1!=r2 else grid[r1][c1]
            return res+max(
                dp(r1+1,c1,r2+1,c2),
                dp(r1+1,c1,r2,c2+1),
                dp(r1,c1+1,r2+1,c2),
                dp(r1,c1+1,r2,c2+1)
            )
        return max(dp(0,0,0,0),0)


# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         n=len(grid)
#         @cache
#         def dp(r1,r2,k):
#             if r1==n or r2==n: return -inf
#             c1,c2=k-r1,k-r2
#             if c1==n or c2==n: return -inf
#             if grid[r1][c1]==-1 or grid[r2][c2]==-1: return -inf
#             if k==2*n-2: return grid[n-1][n-1]
#             res=grid[r1][c1]+grid[r2][c2] if r1!=r2 else grid[r1][c1]
#             return res+max(
#                 dp(r1+1,r2,k+1),
#                 dp(r1,r2+1,k+1),
#                 dp(r1,r2,k+1),
#                 dp(r1+1,r2+1,k+1),
#             )
#         return max(dp(0,0,0),0)

# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         n=len(grid)
#         @cache
#         def dp(r1,r2,k):
#             if r1==n or r2==n or r1<r2: return -inf
#             c1,c2=k-r1,k-r2
#             if c1==n or c2==n: return -inf
#             if grid[r1][c1]==-1 or grid[r2][c2]==-1: return -inf
#             if k==2*n-2: return grid[n-1][n-1]
#             res=grid[r1][c1]+grid[r2][c2] if r1!=r2 else grid[r1][c1]
#             return res+max(
#                 dp(r1+1,r2,k+1),
#                 dp(r1,r2+1,k+1),
#                 dp(r1,r2,k+1),
#                 dp(r1+1,r2+1,k+1),
#             )
#         return max(dp(0,0,0),0)
