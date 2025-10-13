# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        
#         for i in range(m-1,-1,-1): nums1[i+n]=nums1[i]
#         ind,i,j,m=0,n,0,m+n
#         while i<m and j<n:
#             if nums1[i]<nums2[j]:
#                 nums1[ind]=nums1[i]
#                 i+=1
#             else:
#                 nums1[ind]=nums2[j]
#                 j+=1
#             ind+=1
#         while i<m: 
#             nums1[ind]=nums1[i]
#             ind+=1;i+=1
#         while j<n:
#             nums1[ind]=nums2[j]
#             ind+=1;j+=1

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        
#         ind=len(nums1)-1
#         i,j=m-1,n-1
#         while i>=0 and j>=0:
#             if nums1[i]<nums2[j]:
#                 nums1[ind]=nums2[j]
#                 j-=1
#             else:
#                 nums1[ind]=nums1[i]
#                 i-=1
#             ind-=1
#         if j!=-1: nums1[:j+1]=nums2[:j+1]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ind=len(nums1)-1
        i,j=m-1,n-1
        while j>=0:
            if i==-1 or nums1[i]<nums2[j]:
                nums1[ind]=nums2[j]
                j-=1
            else:
                nums1[ind]=nums1[i]
                i-=1
            ind-=1