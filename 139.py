# class Solution:
#     def wordBreak(self, s: str, words: List[str]) -> bool:
        
#         words=set(words)
#         n=len(s)

#         @cache
#         def dp(i):
#             if i==n: return True
#             for j in range(i,n):
#                 cand=s[i:j+1]
#                 if cand in words and dp(j+1): return True
#             return False
        
#         return dp(0)

# class Solution:
#     def wordBreak(self, s: str, words: List[str]) -> bool:
        
#         words=set(words)
#         wordlens=set(len(word) for word in words)
#         n=len(s)

#         @cache
#         def dp(i):
#             if i==n: return True
#             for l in wordlens:
#                 end=min(i+l,n)
#                 cand=s[i:end]
#                 if cand in words and dp(end): return True
#             return False
        
#         return dp(0)


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        
        words=set(words)
        n=len(s)

        @cache
        def dp(i):
            if i==n: return True
            for word in words:
                l=len(word)
                if s[i:i+l]==word and dp(i+l): return True
            return False
        
        return dp(0)