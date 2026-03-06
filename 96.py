# class Solution:
#     def numTrees(self, n: int) -> int:
        
#         @cache
#         def dp(l,r):
#             if l>=r: return 1 
#             res=0
#             for m in range(l,r+1):
#                 res+=dp(l,m-1)*dp(m+1,r)
#             return res
#         return dp(1,n)

class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dp(n):
            if n<=1: return 1 
            res,numchild=0,n-1
            for l in range(numchild+1):
                res+=dp(l)*dp(numchild-l)
            return res
        return dp(n)