# class Solution:
#     def triangularSum(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         for i in range(n):
#             for j in range(n-i-1):
#                 nums[j]=(nums[j]+nums[j+1])%10

#         return nums[0]

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n,res=len(nums),0
        for i in range(n):
            res=(res+comb(n-1,i)*nums[i])%10
        return res
