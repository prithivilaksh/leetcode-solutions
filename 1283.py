# class Solution:
#     def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
#         def getSum(d):
#             return sum(ceil(x/d) for x in nums)
        
#         l,r=1,max(nums)
#         while l<r:
#             m=l+(r-l)//2
#             if getSum(m)<=threshold: r=m
#             else: l=m+1
        
#         return r

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def getSum(d):
            return sum(ceil(x/d) for x in nums)
        
        l,r=ceil(min(nums)/threshold),max(nums)
        while l<r:
            m=l+(r-l)//2
            if getSum(m)<=threshold: r=m
            else: l=m+1
        
        return r