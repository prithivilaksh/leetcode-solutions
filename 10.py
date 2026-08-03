# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         m,n=len(s),len(p)
#         @cache
#         def helper(i,j):
#             if j==-1: return i==-1

#             if p[j]=="*":
#                 c=p[j-1]
#                 if helper(i,j-2): return True
#                 for k in range(i,-1,-1):
#                     if c==".": 
#                         if helper(k-1,j-2):return True
#                     elif s[k]==c: 
#                         if helper(k-1,j-2): return True
#                     else: break
#             if i==-1: return False
#             if p[j]=="." or s[i]==p[j]:
#                 if helper(i-1,j-1): return True
            


#             return False
#         return helper(m-1,n-1)

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         m,n=len(s),len(p)
#         @cache
#         def helper(i,j):
#             if j==-1: return i==-1

#             if p[j]=="*":
#                 c=p[j-1]
#                 if helper(i,j-2): return True
#                 for k in range(i,-1,-1):
#                     if c=="." or s[k]==c: 
#                         if helper(k-1,j-2):return True
#                     else: break
#             if i==-1: return False
#             if p[j]=="." or s[i]==p[j]:
#                 if helper(i-1,j-1): return True
            


#             return False
#         return helper(m-1,n-1)


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:

#         m,n=len(s),len(p)
#         @cache
#         def helper(i,j):
#             if j==-1: return i==-1

#             res=False
            
#             if p[j]=="*":
#                 isCharMatch= i>=0 and (p[j-1]==s[i] or p[j-1]==".")
#                 res= helper(i,j-2) or (isCharMatch and helper(i-1,j))
#             elif i>=0 and p[j]==s[i] or p[j]==".":
#                 res=helper(i-1,j-1)
#             return res

#         return helper(m-1,n-1)


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:

#         m,n=len(s),len(p)
#         dp=[[False]*(n+1) for i in range(m+1)]
#         dp[0][0]=True

#         for j in range(2,n+1): 
#             dp[0][j]= p[j-1]=="*" and dp[0][j-2]

#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if s[i-1]==p[j-1] or p[j-1]=='.':
#                     dp[i][j]= dp[i-1][j-1]
                
#                 elif p[j-1]=="*":
#                     dp[i][j] = dp[i][j-2] or ((s[i-1]==p[j-2] or p[j-2]==".") and dp[i-1][j])


#         return dp[m][n]



# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:

#         m,n=len(s),len(p)
#         dp=[[False]*(n+1) for i in range(m+1)]
#         dp[m][n]=True

#         for j in range(n-1,-1,-1):
#             if p[j]=="*":
#                 dp[m][j-1]=dp[m][j+1]
        
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if j+1<n and p[j+1]=="*":
#                     dp[i][j]=dp[i][j+2] or ((s[i]==p[j] or p[j]==".") and  dp[i+1][j] )
#                 elif s[i]==p[j] or p[j]==".":
#                     dp[i][j]=dp[i+1][j+1]
        
#         return dp[0][0]



# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:

#         m,n=len(s),len(p)
#         @cache
#         def helper(i,j):
#             # if i==m or j==n: 
#             #     if i==m and j==n: return True
#             #     if j==n: return False
            
#             if j==n: return i==m

#             res=False
#             # j should never be *
#             if j+1<n and p[j+1]=="*":
#                 if helper(i,j+2): return True
#                 if i<m and (s[i]==p[j] or p[j]==".") and helper(i+1,j): return True
            
#             # if i and j are matching
#             elif i<m and (s[i]==p[j] or p[j]=="."):
#                 if helper(i+1,j+1): return True
#             return False
            


#         return helper(0,0)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m,n=len(s),len(p)
        @cache
        def helper(i,j):
            if j==n: return i==m

            res=False
            isCharMatch=i<m and (s[i]==p[j] or p[j]==".")
            if j+1<n and p[j+1]=="*":
                res=helper(i,j+2) or (isCharMatch and helper(i+1,j))
            else: res=isCharMatch and helper(i+1,j+1)

            return res
            


        return helper(0,0)







class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dp(i,j):
            if j==-1: return i==-1
            if i>=0 and (p[j]=='.' or s[i]==p[j]): return dp(i-1,j-1)
            if p[j]=='*':
                return dp(i,j-2) or (i>=0 and (p[j-1]==s[i] or p[j-1]=='.') and dp(i-1,j))
            return False
        
        return dp(len(s)-1,len(p)-1)


