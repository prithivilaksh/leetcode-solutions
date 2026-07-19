class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1
        while l<r:
            m=l+(r-l)//2
            # if nums[l]<nums[r]: return nums[l]
            if nums[m]>nums[r]: l=m+1
            else: r=m
        return nums[r]



# class Solution:
#     def findMin(self, nums: List[int]) -> int:
        
#         #  /
#         # /
#         #          /
#         #         /

#         l,r=0,len(nums)-1

#         while l<r:
#             m=l+(r-l)//2
#             if nums[l]>nums[m]: r=m
#             else: #nums[l]<nums[m]
#                 if nums[r]<nums[l] : l=m+1
#                 else: r=m
        
#         return nums[l]

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
        
#         #  /
#         # /
#         #          /
#         #         /

#         l,r=0,len(nums)-1

#         while l<r:
#             m=l+(r-l)//2
#             if nums[l]<nums[r]: break
#             if nums[l]>nums[m]: r=m
#             else: l=m+1
        
#         return nums[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1

        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[r]: l=m+1
            else: r=m
        
        return nums[l]
