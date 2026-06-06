# class Solution:
#     def search(self, nums: List[int], t: int) -> int:
        
#         l,r=0,len(nums)-1
#         while l<=r:
#             m=l+(r-l)//2
#             if nums[m]==t: return m
#             if t<nums[m]:
#                 if nums[l]<=t or nums[m]<nums[r]: r=m-1
#                 else: l=m+1
#             elif nums[m]<t:
#                 if nums[l]<nums[m] or t<=nums[r]: l=m+1
#                 else: r=m-1
        
#         return -1

# class Solution:
#     def search(self, nums: List[int], t: int) -> int:

#         l,r=0,len(nums)-1
#         while l<r:
#             m=l+(r-l)//2
#             if nums[m]<=nums[r]:r=m
#             else: l=m+1
        
#         if nums[-1]<t: l,r=0,r-1
#         else: r=len(nums)-1

#         while l<=r:
#             m=l+(r-l)//2
#             if nums[m]==t: return m
#             if t<nums[m]: r=m-1
#             else: l=m+1
#         return -1

# class Solution:
#     def search(self, nums: List[int], t: int) -> int:

#         # idea/observation:
#         # 1) distinct values
#         # 2) 1<=k<n
#         # 3) visualization
#         #      /|
#         #     / |
#         #       | /
#         #       |/
        
#         l,r=0,len(nums)-1
#         while l<=r:
#             m=l+(r-l)//2
#             if nums[m]==t: return m
#             if nums[m]<t:
#                 if nums[l]<=nums[m] or t<=nums[r]: l=m+1
#                 else: r=m-1
#             else: # nums[m]>t
#                 if nums[l]<=t or nums[m]<=nums[r] : r=m-1
#                 else: l=m+1
#         return -1


class Solution:
    def search(self, nums: List[int], t: int) -> int:
        
        #  /
        # /
        #     /
        #    /
        l,r=0,len(nums)-1

        while l<=r:
            m=l+(r-l)//2
            if nums[m]==t: return m
            if nums[m]<t:
                if nums[l]<=nums[m] or t<nums[l]:l=m+1
                else: r=m-1
            else:
                if nums[l]<=t or nums[m]<nums[l]:r=m-1
                else: l=m+1
        
        return -1
















        
      