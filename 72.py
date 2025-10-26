class Solution:
    def minDistance(self, a: str, b: str) -> int:
        
        m,n=len(a),len(b)

        @cache
        def dp(i,j):
            if i==m: return n-j
            if j==n: return m-i

            if a[i]==b[j]: return dp(i+1,j+1)
            return 1+min(dp(i+1,j),dp(i,j+1),dp(i+1,j+1))
        
        return dp(0,0)


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
        
#         m,n=len(word1),len(word2)
#         @cache
#         def helper(i,j):
#             if i==m or j==n: return max(m-i,n-j)
#             res=inf
#             if word1[i]==word2[j]: res=min(res,helper(i+1,j+1))
#             res=min(res,1+helper(i,j+1),1+helper(i+1,j),1+helper(i+1,j+1))
#             return res
        
#         return helper(0,0)

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
        
#         m,n=len(word1),len(word2)
#         @cache
#         def helper(i,j):
#             if i==m or j==n: return max(m-i,n-j)
#             if word1[i]==word2[j]: return helper(i+1,j+1)
#             return 1+min(helper(i,j+1),helper(i+1,j),helper(i+1,j+1))
        
#         return helper(0,0)
        


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
        
#         m,n=len(word1),len(word2)
#         dp=[[0]*(n+1) for i in range(m+1)]
#         for i in range(m-1,-1,-1):dp[i][n]=m-i
#         for j in range(n-1,-1,-1):dp[m][j]=n-j
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if word1[i]==word2[j]: dp[i][j]=dp[i+1][j+1]
#                 else: dp[i][j]=1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
        
#         return dp[0][0]

