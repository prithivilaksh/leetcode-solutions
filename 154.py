# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if not nums: return inf

#         l,r=0,len(nums)-1

#         while l<r:
#             m=l+(r-l)//2
#             if nums[l]==nums[m]==nums[r]: return min(self.findMin(nums[l:m]),self.findMin(nums[m+1:r+1]))
#             if nums[l]<nums[r]: return nums[l]
#             if nums[m]>nums[r]: l=m+1
#             else: r=m
#         return nums[r]

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r=0,len(nums)-1
        while l<r:
            m=l+(r-l)//2
            # if nums[l]<nums[r]: return nums[l]
            if nums[m]==nums[r]: r-=1
            elif nums[m]>nums[r]: l=m+1
            else: r=m
        return nums[r]