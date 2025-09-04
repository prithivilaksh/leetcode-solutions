# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
#         m,n,tot=len(s1),len(s2),len(s3)
#         if m+n!=tot: return False
        
#         dp=[[False] * (n+1) for i in range(m+1)]
#         dp[m][n]=True
#         for i in range(m-1,-1,-1):dp[i][n]=s1[i]==s3[i+n] and dp[i+1][n]
#         for j in range(n-1,-1,-1):dp[m][j]=s2[j]==s3[m+j] and dp[m][j+1]

#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                     dp[i][j]= (s1[i]==s3[i+j] and dp[i+1][j]) or (s2[j]==s3[i+j] and dp[i][j+1])
        
#         return dp[0][0]

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m,n,tot=len(s1),len(s2),len(s3)
#         if m+n!=tot: return False
#         @cache
#         def dp(i,j):
#             if i==m and j==n: return True
#             if i!=m and s1[i]==s3[i+j] and dp(i+1,j): return True
#             if j!=n and s2[j]==s3[i+j] and dp(i,j+1): return True
        
#         return bool(dp(0,0))

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m,n,tot=len(s1),len(s2),len(s3)
        if m+n!=tot: return False
        
        dp=[[False] * (n+1) for i in range(m+1)]
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                    dp[i][j]= (i!=m and s1[i]==s3[i+j] and dp[i+1][j]) or \
                              (j!=n and s2[j]==s3[i+j] and dp[i][j+1]) or \
                              (i==m and j==n)
        
        return dp[0][0]