# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:


#         nums.sort()
#         n=len(nums)
#         l,r=0,n-1

#         def remove(x):
#             l,r=0,n-1-x
#             for i in range(x+1):
#                 if nums[r+i]<=nums[l+i]*k:
#                     return True
#             return False
        
#         res=n-1
#         while l<=r:
#             m=l+(r-l)//2
#             if remove(m):
#                 res=m
#                 r=m-1
#             else: l=m+1

#         return res
                

# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:


#         nums.sort()
#         n=len(nums)
#         l,r=0,n-1

#         def remove(x):
#             l,r=0,n-1-x
#             for i in range(x+1):
#                 if nums[r+i]<=nums[l+i]*k:
#                     return True
#             return False
        
#         while l<r:
#             m=l+(r-l)//2
#             if remove(m):r=m
#             else: l=m+1

#         return r

# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:

#         nums.sort()
#         n=len(nums)
#         l=r=res=0
#         for r,_ in enumerate(nums):
#             if nums[l]*k<nums[r]: l+=1
#             res=max(res,r-l+1)
        
#         return n-res

# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:

#         nums.sort()
#         n=len(nums)
#         l=r=0
#         for r,_ in enumerate(nums):
#             if nums[l]*k<nums[r]: l+=1
        
#         return n-(r-l+1)

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        nums.sort()
        l=r=0
        for r,_ in enumerate(nums):
            if nums[l]*k<nums[r]: l+=1
        
        return l
            

        
                