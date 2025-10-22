# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         n=len(nums)
#         left=bisect_left(nums,target)
#         if left==n or nums[left]!=target: return [-1,-1]
#         right=bisect_right(nums,target)-1
#         return [left,right]

class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        
        n=len(nums)

        def bisectleft(x):
            l,r=0,n
            while l<r:
                m=l+(r-l)//2
                if nums[m]>=x: r=m
                else: l=m+1
            return r
        
        l,r=bisectleft(t),bisectleft(t+1)-1
        return [l,r] if l<=r else [-1,-1]        
