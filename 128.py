# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         nums=set(nums)
#         @cache
#         def dp(x):
#             if x not in nums: return 0
#             return 1+dp(x-1)
            
#         return max([dp(x) for x in nums],default=0)

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         nums,res=set(nums),0
#         starts=[x for x in nums if x-1 not in nums]
#         for l in starts:
#             r=l
#             while r+1 in nums: r+=1
#             res=max(res,r-l+1)
#         return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums,res=set(nums),0
        for l in nums:
            if l-1 not in nums:
                r=l
                while r+1 in nums: r+=1
                res=max(res,r-l+1)
        return res