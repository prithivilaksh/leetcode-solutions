class Solution:
    def minXor(self, nums: List[int], k: int) -> int:

        n=len(nums)
        @lru_cache(None)
        def helper(pos,rem):
            if pos==n and rem==0: return 0
            if pos==n or rem==0: return float('inf')

            rxor,res=0,float('inf')
            for i in range(pos,n-rem+1):
                rxor^=nums[i]
                if rxor>=res: continue
                mx=max(rxor,helper(i+1,rem-1))
                res=min(res,mx)
            return res

        return helper(0,k)
