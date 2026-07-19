# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         low = 0
#         n = len(nums)
#         high = n - 1
#         while low <= high:
#             mid = low + (high - low)//2
#             if nums[mid]==target: return True
#             if nums[low] == nums[mid] == nums[high]:
#                 low +=1;high -=1
        
#             elif nums[low] <= nums[mid]:
#                 if nums[low] <= target < nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 if nums[mid] < target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
        
#         return False
                

class Solution:
    def search(self, nums: List[int], t: int) -> bool:


        # idea/observation:
        # 1) duplicate values are allowed
        # 2) 0<=k<n
        # 3) Visualization
        #        __/|
        #     __/   |    __
        #           | __/
        #           |/
        #     if k==0
        #      __/
        #     /
        #     if k==n-1
        #     .
        #     | __/
        #     |/

        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==t: return True
            if nums[m]==nums[r]: r-=1;continue
            if nums[m]<t:
                if nums[l]<=nums[m] or t<=nums[r]: l=m+1
                else: r=m-1
            else: #nums[m]>t
                if nums[l]<=t or nums[m]<=nums[r]:r=m-1
                else: l=m+1
        return False












class Solution:
    def search(self, nums: List[int], t: int) -> bool:
        
    #      _/
    #    _/
    #           _/
    #         _/
        
        l,r=0,len(nums)-1

        while l<=r:
            m=l+(r-l)//2
            if nums[m]==t: return True
            if nums[l]==nums[m]: l+=1;continue
            if nums[m]<t:
                if nums[l]<=nums[m] or t<nums[l]:l=m+1
                else: r=m-1
            else:
                if nums[l]<=t or nums[m]<nums[l]:r=m-1
                else: l=m+1

        return False


# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
        
#     #           ____
#     #      ____/
#     # ____/                          ____
#     #                           ____/
#     #                      ____/

#         l,r=0,len(nums)-1

#         while l<=r:
#             m=l+(r-l)//2
#             if nums[m]==target: return True
#             if nums[r]==nums[m]: r-=1;continue
#             if nums[m]<target:
#                 if target<=nums[r] or nums[r]<nums[m]:l=m+1
#                 else: r=m-1
#             else: #nums[m]>target
#                 if nums[m]<nums[r] or nums[r]<target: r=m-1
#                 else: l=m+1
        
#         return False


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
    #           ____
    #      ____/
    # ____/                          ____
    #                           ____/
    #                      ____/

        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target: return True
            
            if nums[m]==nums[r]: r-=1
            elif nums[m]<nums[r]:
                if target<nums[m] or target>nums[r]: r=m-1
                else: l=m+1
            else: #nums[m]>nums[r]
                if target<=nums[r] or nums[m]<target: l=m+1
                else: r=m-1

        
        return False