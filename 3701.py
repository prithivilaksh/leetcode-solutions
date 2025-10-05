class Solution:
    def alternatingSum(self, nums: List[int]) -> int:

        res=0
        sign=1
        for x in nums:
            res+=sign*x
            sign*=-1
        return res