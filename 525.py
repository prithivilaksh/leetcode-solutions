class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        f={0:-1}
        rsum=res=0
        for r,x in enumerate(nums):
            rsum+= 1 if x==1 else -1
            if rsum in f: res=max(res,r-f[rsum])
            else: f[rsum]=r
        
        return res