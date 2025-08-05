# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         m,n=len(s),len(p)
#         @cache
#         def dp(i,j):
#             if j==n: return i==m
#             if p[j]=="*":
#                 if dp(i,j+1): return True
#                 if i+1<=m and dp(i+1,j): return True
#             elif p[j]=="?" and dp(i+1,j+1): return True
#             elif i<m and s[i]==p[j] and dp(i+1,j+1): return True
#             return False
#         return dp(0,0)

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         m,n=len(s),len(p)
#         @cache
#         def dp(i,j):
#             if j==n: return i==m
#             if p[j]=="*":
#                 if dp(i,j+1) or (i<m and dp(i+1,j)): return True
#             elif (p[j]=="?" or (i<m and s[i]==p[j])) and dp(i+1,j+1): return True

#         return bool(dp(0,0))


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         m,n=len(s),len(p)
#         dp=[False]*(n+1)

#         dp[n]=True
#         for j in range(n-1,-1,-1):
#             if p[j]=="*": dp[j]=dp[j+1]
#             else: break

#         for i in range(m-1,-1,-1):
#             dp[n]=False
#             dpi1j1=i==m-1
#             for j in range(n-1,-1,-1):
#                 dpij=dp[j]
#                 if p[j]=="*":
#                     dp[j]=dpij or dp[j+1]
#                 else :
#                     dp[j]=(s[i]==p[j] or p[j]=="?") and dpi1j1
#                 dpi1j1=dpij

#         return dp[0]


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         m,n=len(s),len(p)
#         dp=[[False]*(n+1) for i in range(m+1)]

#         dp[m][n]=True
#         for j in range(n-1,-1,-1):
#             if p[j]=="*": dp[m][j]=dp[m][j+1]
#             else: break

#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if p[j]=="*":
#                     dp[i][j]=dp[i][j+1] or dp[i+1][j]
#                 elif s[i]==p[j] or p[j]=="?":
#                     dp[i][j]=dp[i+1][j+1]

#         return dp[0][0]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m,n=len(s),len(p)
        i,j=0,0
        nexti,nextj=-1,-1

        while i<m:
            if j<n and (s[i]==p[j] or p[j]=="?"): i+=1;j+=1
            elif j<n and p[j]=="*":
                nexti=i+1
                nextj=j+1
                j+=1
            elif nextj!=-1:
                i=nexti
                j=nextj
                nexti+=1
            else: return False
        while j<n and p[j]=="*":j+=1
        return j==n
