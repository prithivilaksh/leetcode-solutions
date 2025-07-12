# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         z=o=t=0
#         for x in nums:
#             if x==0:
#                 nums[t]=nums[t-1]
#                 nums[o]=nums[o-1]
#                 nums[z]=0
#                 t+=1;o+=1;z+=1
#             elif x==1:
#                 nums[t]=nums[t-1]
#                 nums[o]=1
#                 t+=1;o+=1
#             else:
#                 nums[t]=2
#                 t+=1

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         z=o=t=0
#         for x in nums:
#             if x==0:
#                 nums[t]=2
#                 nums[o]=1
#                 nums[z]=0
#                 t+=1;o+=1;z+=1
#             elif x==1:
#                 nums[t]=2
#                 nums[o]=1
#                 t+=1;o+=1
#             else:
#                 nums[t]=2
#                 t+=1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=o=t=0
        for x in nums:
            nums[t]=2
            t+=1
            if x<=1:
                nums[o]=1
                o+=1
            if x==0:
                nums[z]=0
                z+=1
        

        
        