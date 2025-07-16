# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
        
#         n=len(nums)

#         for i,x in enumerate(nums):
#             if x<=0: nums[i]=n+1

#         for i,x in enumerate(nums):
#             x=abs(x)
#             if x<=n:
#                 nums[x-1]=-abs(nums[x-1])
                
#         for i,x in enumerate(nums):
#             if x>0: return i+1
        
#         return n+1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
    #    res will be in range [1,n+1]
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]

        for i,x in enumerate(nums):
            if x!=i+1: return i+1
        
        return n+1