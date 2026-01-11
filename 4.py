# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

#         # notes:
#         #     0 to m-1, 0 to n-1
#         #     l1cnt+r1cnt=m
#         #     l1cnt=m1-0+1=m1+1
#         #     r1cnt=m-l1cnt=m-m1-1

#         #     l2cnt+r2cnt=n
#         #     l2cnt=m2-0+1=m2+1
#         #     r2cnt=n-l2cnt=n-m2-1

#         #     if m+n is even
#         #     l1cnt+l2cnt = r1cnt+r2cnt
#         #     m1+1+m2+1 = m-m1-1+n-m2-1
#         #     m1+m2+2 = m-m1-m2+n-2
#         #     2 m2 = m-2 m1 +n -4
#         #       m2 = (m+n-4)//2 -m1
#         #       m2 = (m+n-2)//2 -m1 -1
#         #       in python after accounting for floor divison
#         #       m2 = (m+n-1)//2 -m1 -1

#         #     or
#         #     if m+n is odd keep the left side bigger
#         #     l1cnt+l2cnt=1+r1cnt+r2cnt
#         #     m1+1+m2+1 = 1+m-m1-1+n-m2-1
#         #     m1+m2+2 = m-m1-m2+n-1
#         #     2 m2 = m-2 m1 +n -3
#         #       m2 = (m+n-3)//2 -m1 
#         #       m2 = (m+n-1)//2 -m1 -1


#         if len(nums1)>len(nums2): nums1,nums2=nums2,nums1
#         nums1=[-inf]+nums1+[inf]
#         nums2=[-inf]+nums2+[inf]

#         m,n=len(nums1),len(nums2)
#         l,r=0,m-1

#         while True:
#             m1=l+(r-l)//2
#             m2=(m+n-1)//2 - m1 - 1
#             if nums1[m1]<=nums2[m2+1] and nums2[m2]<=nums1[m1+1]:
#                 if (m+n)%2: return max(nums1[m1],nums2[m2])
#                 return (max(nums1[m1],nums2[m2])+min(nums1[m1+1],nums2[m2+1]))/2    
#             elif nums1[m1] > nums2[m2+1]: r=m1-1
#             else: l=m1+1
        
#         return -1

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:

        # idea/observation:
        # 1) split into two equal halves (left skewed)
        # 2) m,n=len(a),len(b)
        # 3) 0..m1 => m1+1 elements | m1+1..m-1 => m-1-m1 elements
        # 4) 0..m2 => m2+1 elements | m2+1..n-1 => n-1-m2 elements
        # 5) if even:
        #     m1+1+m2+1=m-1-m1+n-1-m2
        #     m1+m2+2 = m+n -m1-m2 - 2
        #     2m2     = m+n -2m1 - 4
        #     m2      = (m+n)//2 -m1 - 2
        # 6) if odd:
        #     m1+1+m2+1=m-1-m1+n-1-m2+1
        #     m1+m2+2 = m+n -m1-m2 - 1
        #     2m2     = m+n -2m1 - 3
        #     2m2     = m+n+1 -2m1 - 4
        #     m2      = (m+n+1)//2 - m1 - 2

        if len(a)>len(b): a,b=b,a # this is very important

        a,b=[-inf]+a+[inf],[-inf]+b+[inf]
        m,n=len(a),len(b)
        isodd=(m+n)%2

        l,r=0,m-1

        while True:

            m1=l+(r-l)//2
            m2=((m+n+isodd)//2) - m1 - 2
            if a[m1]<=b[m2+1] and b[m2]<=a[m1+1]:
                if isodd: return max(a[m1],b[m2])
                else: return (max(a[m1],b[m2]) + min(a[m1+1],b[m2+1]))/2
            elif a[m1]>b[m2+1]: r=m1-1
            else: l=m1+1

# -inf 2    3 4 inf
# - inf 1   inf
















