# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
#         n=len(s)
#         dp=[[0]*n for i in range(n)]
#         res=""

#         for i in range(n-1,-1,-1):
#             for j in range(i,n):
#                 if s[i]==s[j] and (j-i<=1 or dp[i+1][j-1]):
#                     dp[i][j]=1
#                     if j-i+1>len(res): res=s[i:j+1]
        
#         return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)
        res=""
        def expand(l,r):
            while l>=0 and r<n and s[l]==s[r]: l-=1;r+=1
            l+=1;r-=1
            return l,r
        
        for i in range(n):
            l,r=expand(i,i)
            if r-l+1>len(res): res=s[l:r+1]
            l,r=expand(i,i+1)
            if r-l+1>len(res): res=s[l:r+1]

        return res