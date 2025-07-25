# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
        
#         m,n=len(s),len(t)
#         @cache
#         def helper(i,j):
#             if i==n: return 1
#             if n-i>m-j: return 0
#             res=0
#             for k in range(j,m):
#                 if t[i]==s[k]:
#                     res+=helper(i+1,k+1)
#             return res

#         return helper(0,0)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m,n=len(s),len(t)
        @cache
        def helper(i,j):
            if i==n or j==m or n-i>m-j: return int(i==n)
            res=helper(i,j+1)
            if t[i]==s[j]:
                res+=helper(i+1,j+1)
            return res

        return helper(0,0)


# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
        
#         m,n=len(s),len(t)
#         dp=[[0]*(m+1) for i in range(n+1)]
#         for j in range(m+1):dp[n][j]=1
        
#         for i in range(n-1,-1,-1):
#             for j in range(m-1,-1,-1):
#                 dp[i][j]=dp[i][j+1]
#                 if t[i]==s[j]:
#                     dp[i][j]+=dp[i+1][j+1]

#         return dp[0][0]
            

