# class Solution:
#     def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
#         mod=10**9+7
#         asum,n=0,len(nums1)
#         for a,b in zip(nums1,nums2):
#             asum=(asum+abs(a-b))%mod
        
#         sortednums1=sorted(nums1)
#         mxd=0
#         for i,x in enumerate(nums2):
#             pos=bisect_left(sortednums1,x)
#             cand=[]
#             if pos<n: cand.append(sortednums1[pos])
#             if pos-1>=0: cand.append(sortednums1[pos-1])

#             for y in cand:
#                 ediff=abs(nums1[i]-x)
#                 ndiff=abs(y-x)
#                 if ediff>ndiff and mxd<ediff-ndiff:
#                     mxd=ediff-ndiff
        
#         return (asum-mxd)%mod

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        snums1=sorted(set(nums1))
        asum,n=0,len(snums1)
        mxd,mod=0,10**9+7
        for a,b in zip(nums1,nums2):
            pos=bisect_left(snums1,b)
            cand=[]
            if pos<n: cand.append(snums1[pos])
            if pos-1>=0: cand.append(snums1[pos-1])

            ediff=abs(a-b)
            asum+=ediff
            for x in cand:
                ndiff=abs(x-b)
                mxd=max(mxd,ediff-ndiff)
        
        return (asum-mxd)%mod