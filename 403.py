class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        stones=set(stones)
        mx=max(stones)
        @cache
        def dp(pos,k):
            if pos==mx: return True
            if pos>mx: return False
            res=False
            for x in (k-1,k,k+1):
                if x>0 and pos+x in stones:
                    res=res or dp(pos+x,x)
            return res
        
        return dp(0,0)