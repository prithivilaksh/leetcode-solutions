# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
        
#         l=zcnt=res=0
#         for r,x in enumerate(nums):
#             if x==0: 
#                 zcnt+=1
#                 while zcnt>k:
#                     if nums[l]==0: zcnt-=1
#                     l+=1
#             res=max(res,r-l+1)
#         return res

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
        
#         l=zcnt=0
#         for r,x in enumerate(nums):
#             if x==0: zcnt+=1
#             if zcnt>k:
#                 if nums[l]==0: zcnt-=1
#                 l+=1
#         return r-l+1

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l=0
        for r,x in enumerate(nums):
            if x==0: k-=1
            if k<0:
                if nums[l]==0: k+=1
                l+=1
        return r-l+1