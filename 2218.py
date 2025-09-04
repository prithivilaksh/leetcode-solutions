class Solution:
    def maxValueOfCoins(self, p: List[List[int]], k: int) -> int:
        n=len(p)
        @cache
        def dp(i,k):
            if i==n or k==0: return 0
            res=dp(i+1,k)
            rsum=0
            for j in range(min(k,len(p[i]))):
                rsum+=p[i][j]
                res=max(res,rsum+dp(i+1,k-j-1))
            return res

        return dp(0,k)


# class Solution:
#     def maxValueOfCoins(self, p: List[List[int]], k: int) -> int:
#         n=len(p)
#         @cache
#         def dp(i,j):
#             if i==n or j==0: return 0
#             res=dp(i+1,j)
#             rsum=0
#             for l in range(1,min(j+1,len(p[i])+1)):
#                 rsum+=p[i][l-1]
#                 res=max(res,rsum+dp(i+1,j-l))
#             return res

#         return dp(0,k)

# class Solution:
#     def maxValueOfCoins(self, p: List[List[int]], k: int) -> int:
#         n=len(p)
#         dp=[[0]*(k+1) for _ in range(n+1)]
#         for i in range(n-1,-1,-1):
#             m=len(p[i])
#             for j in range(k+1):
#                 rsum=0
#                 dp[i][j]=dp[i+1][j]
#                 for l in range(1,min(j+1,m+1)):
#                     rsum+=p[i][l-1]
#                     dp[i][j]=max(dp[i][j],rsum+dp[i+1][j-l])

#         return dp[0][k]