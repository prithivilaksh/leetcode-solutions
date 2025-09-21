class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res=0
        for x in nums:
            if x&1==0:
                res|=x
        return res
                