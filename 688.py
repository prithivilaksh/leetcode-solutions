
## wrong look below
# class Solution:
#     def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        
#         dir=((-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1))
#         @cache
#         def dp(i,j,k):
#             if i<0 or i>=n or j<0 or j>=n: return 0,1
#             if k==0: return 1,0

#             totin=totout=0
#             for di,dj in dir:
#                 vi,vj=i+di,j+dj
#                 inn,out=dp(vi,vj,k-1)
#                 totin+=inn
#                 totout+=out
#             return totin,totout
        
#         totin,totout=dp(r,c,k)
#         print(totin,totout)
#         return totin/(totin+totout)

# class Solution:
#     def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        
#         dir=((-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1))
#         @cache
#         def dp(i,j,k):
#             if i<0 or i>=n or j<0 or j>=n: return 0
#             if k==0: return 1

#             res=0
#             for di,dj in dir:
#                 vi,vj=i+di,j+dj
#                 res+=dp(vi,vj,k-1)
#             return res/8
        
#         return dp(r,c,k)


class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        dirs = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

        @cache
        def dp(i, j, moves):
            if i < 0 or i >= n or j < 0 or j >= n: return 0
            if moves == 0: return 1

            totin=0
            for di, dj in dirs:
                totin += dp(i + di, j + dj, moves - 1)
            return totin
        return dp(r, c, k) / (8 ** k)
