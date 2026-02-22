# class Solution:
#     def minMovesToMakePalindrome(self, s: str) -> int:
#         if len(s)<=1: return 0
#         n=len(s)
#         for l in range(n):
#             c=s[l]
#             r=n-1
#             while l<r and c!=s[r]: r-=1
#             if l==r: continue
#             return l+ (n-1-r) + self.minMovesToMakePalindrome(s[:l]+s[l+1:r]+s[r+1:])


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        
        res,n=0,len(s)
        while n>2:
            l,r=0,s.rfind(s[0])
            n=len(s)
            if l==r: 
                res+=n//2
                s=s[1:n//2 +1]+s[n//2 +1:]
            else:
                res+=n-1-r
                s=s[1:r]+s[r+1:]
        return res