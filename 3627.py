# class Solution:
#     def maximumMedianSum(self, nums: List[int]) -> int:


#         nums.sort()
#         n,res = len(nums),0
#         for i in range(n-2,n//3 -1 ,-2):
#             res+=nums[i]
#         return res

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        
        nums.sort()
        n,res = len(nums),0
        for i in range(n//3, n, 2):
            res += nums[i]
        return res
