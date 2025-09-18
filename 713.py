# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         if k==0: return 0
#         p=1
#         res=l=0
#         for r,x in enumerate(nums):
#             p*=x
#             while l<=r and p>=k:
#                 p//=nums[l]
#                 l+=1
#             if l<=r: res+=r-l+1
#         return res

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        p,l,res=1,0,0
        for r,x in enumerate(nums):
            p*=x
            while p>=k:
                p//=nums[l]
                l+=1
            res+=r-l+1
        return res