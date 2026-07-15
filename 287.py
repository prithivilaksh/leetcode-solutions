class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            pos=abs(nums[i])-1
            if nums[pos]<0: return pos+1
            nums[pos]=-nums[pos]
