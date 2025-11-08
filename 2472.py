# class Solution:
#     def maxPalindromes(self, s: str, k: int) -> int:
        

#         n=len(s)
#         @cache
#         def dp(i):
#             res=0
#             if i+k-1<n:
#                 res=dp(i+1)
#                 res=max(res,(s[i:i+k]==s[i:i+k][::-1]) +  dp(i+k))
#             if i+k+1-1<n: 
#                 res=max(res,(s[i:i+k+1]==s[i:i+k+1][::-1]) +  dp(i+k+1))
#             return res
        
#         return dp(0)

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n=len(s)
        def dp(i):
            if i+k-1<n and s[i:i+k]==s[i:i+k][::-1]: return 1+dp(i+k)
            if i+k+1-1<n and s[i:i+k+1]==s[i:i+k+1][::-1]: return 1+dp(i+k+1)
            if i+k<n: return dp(i+1)
            return 0
        return dp(0)

        