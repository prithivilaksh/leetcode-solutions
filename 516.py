# import sys
# sys.setrecursionlimit(10**8)
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
        
#         @cache
#         def dp(i,j):
#             if i==j: return 1
#             if i>j: return 0
#             res=0 
#             if s[i]==s[j]: res=dp(i+1,j-1)+2
#             res=max(res,dp(i,j-1),dp(i+1,j))
#             return res
        
#         return dp(0,len(s)-1)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dp(i,j):
            if i==j: return 1
            if i>j: return 0
            if s[i]==s[j]: return dp(i+1,j-1)+2
            return max(dp(i,j-1),dp(i+1,j))
        
        return dp(0,len(s)-1)


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
    
#         n=len(s)
#         dp=[[0]*n for _ in range(n)]
#         for i in range(n): dp[i][i]=1

#         for i in range(n-1,-1,-1):
#             for j in range(i+1,n):
#                 if s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
#                 else: dp[i][j]=max(dp[i][j-1],dp[i+1][j])

#         return dp[0][n-1]
