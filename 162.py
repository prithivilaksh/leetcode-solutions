class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums=[-inf]+nums+[-inf]
        l,r=1,len(nums)-2

        while l<=r:
            m=l+(r-l)//2
            if nums[m-1]<nums[m]>nums[m+1]: return m-1
            elif nums[m-1]<nums[m]: l=m+1
            elif nums[m]>nums[m+1]: r=m-1
            # else: l=m+1
            else: r=m-1
