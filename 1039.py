class Solution:
    def minScoreTriangulation(self, val: List[int]) -> int:
        
        n=len(val)
        @cache
        def dp(l,r):
            if l+1==r: return 0
            res=inf
            for m in range(l+1,r):
                res=min(res,dp(l,m)+(val[l]*val[m]*val[r])+dp(m,r))
            
            return res
        
        return dp(0,n-1)