# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
        
#         n=len(s)
#         rev=s[::-1]
#         for i in range(n):
#             if s[:n-i]==rev[i:]:
#                 return rev[:i]+s
#         return rev+s

# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
        
#         n=len(s)
#         for i in range(n):
#             if s[:n-i]==s[:n-i][::-1]:
#                 return s[::-1][:i]+s
#         return s[::-1]+s

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # observation/idea:
        #     1) find the longest palindrome from the beginning
        #     2) add the reverse of remaining characters at the beginning
        
        # Finding Longest palindrome from the beginning
        #     1) KMP Algorithm
        #     2) s is our pattern
        #     3) reverse(s) is our string
        #     4) i goes from left to right and j goes from right to left
        #     4) if i==j or i==j-1 : then it is the longest palindrome from beginning

        #     abcdefgdcba
        #     abcdgfedcba
        n=len(s)
        lps=[0]*n
        i,j=0,1
        while j<n:
            if s[i]==s[j]:
                lps[j]=i+1
                i+=1
                j+=1
            elif i!=0: i=lps[i-1]
            else: j+=1
        
        i,j=0,n-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            elif i!=0: i=lps[i-1]
            else: j-=1
        
        if i==j: return s[2*i+1:][::-1]+s
        i-=1;j+=1
        return s[2*i+2:][::-1]+s 


# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
        
#         n=len(s)
#         lps=[0]*n

#         i,j=0,1
#         while j<n:
#             if s[i]==s[j]:
#                 lps[j]=i+1
#                 i+=1
#                 j+=1
#             elif i!=0: i=lps[i-1]
#             else: j+=1
        
#         i,j=0,n-1
#         while i<j:
#             if s[i]==s[j]:
#                 i+=1
#                 j-=1
#             elif i!=0: i=lps[i-1]
#             else: j-=1
#         if i==j: return s[2*i+1:][::-1]+s
#         return s[2*i:][::-1]+s
    
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)

        for c in s[::-1]:
            if c == s[i]:
                i += 1

        if i == n: return s
        
        sub = s[i:]
        return sub[::-1] + self.shortestPalindrome(s[:i]) + sub
        