class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1
        while l<r:
            m=l+(r-l)//2
            if m%2==0:
                if nums[m]==nums[m+1]:l=m+2
                else: r=m
            else:
                if nums[m-1]==nums[m]:l=m+1
                else: r=m-1
        return nums[r]