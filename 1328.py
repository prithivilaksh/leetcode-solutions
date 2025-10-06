# class Solution:
#     def breakPalindrome(self, s: str) -> str:
#         # idea/observation:
#         #     1) To make it lexicographically smaller, replace a potential char with a
#         #     2) If all the characters are "a", then replace the last char with b
#         #     3) As the resulting string should not be a palindrome, make sure the position is not the exact middle
#         n=len(s)
#         mid=-1 if n%2==0 else n//2
#         for i,x in enumerate(s):
#             if x!='a' and i!=mid:
#                 return s[:i]+'a'+s[i+1:]
#         if mid==n-1: return ""
#         return s[:-1]+'b'


class Solution:
    def breakPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1: return ""
        for i in range(n//2):
            if s[i] != 'a': return s[:i] + 'a' + s[i+1:]
        return s[:-1] + 'b'