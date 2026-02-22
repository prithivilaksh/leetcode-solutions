# class Solution:
#     def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
#         nums.sort()
#         def check(dis):
#             res=0
#             for l,x in enumerate(nums):
#                 r=bisect_right(nums,x+dis,lo=l+1)-1
#                 res+= r - (l+1) +1
#                 if res>=k: return True
#             return False
        
#         l,r,res=0,nums[-1]-nums[0],0
#         while l<=r:
#             m=l+(r-l)//2
#             if check(m): res,r=m,m-1
#             else: l=m+1
#         return res


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n=len(nums)
        def check(dis):
            res=l=0
            for r in range(n):
                while nums[r]-nums[l]>dis: l+=1
                res+=r-l
            return res>=k
        
        l,r,res=0,nums[-1]-nums[0],0
        while l<=r:
            m=l+(r-l)//2
            if check(m): res,r=m,m-1
            else: l=m+1
        return res