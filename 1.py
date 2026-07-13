class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind={}
        for i,x in enumerate(nums):
            if target-x in ind: return [ind[target-x],i]
            ind[x]=i