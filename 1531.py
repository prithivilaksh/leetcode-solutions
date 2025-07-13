
# s -> char + count if count>1 else char

# delete at most k from s to minimize compressed length of s
        
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        n=len(s)
        compLength = lambda x: 1 if x==1 else 2 if x<=9 else 3 if x<=99 else 4

        @cache
        def helper(l,k):
            if n-l<=k: return 0 # delete remaining
            mp=defaultdict(int)
            mx,res=0,104
            for r in range(l,n):
                mp[s[r]]+=1
                mx=max(mx,mp[s[r]])
                if k < r-l+1-mx: break # even if mx increases r will also increase making the combinations invalid
                res=min(res,compLength(mx)+helper(r+1,k-(r-l+1-mx)))
            
            return res
        return helper(0,k)
