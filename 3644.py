class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res=-1
        for i,x in enumerate(nums):
            if i!=x: res&=x
        return res if res!=-1 else 0
