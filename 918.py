# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:

#         if max(nums)<=0: return max(nums)

#         n=len(nums)
#         res=sum=0
#         for i,x in enumerate(nums):
#             if sum+x>0: sum+=x
#             else: sum=0
#             res=max(res,sum)
        
#         pre,suf=[0]*n,[0]*n

#         pre[0],suf[n-1]=nums[0],nums[n-1]
#         for i in range(1,n):
#             pre[i]=pre[i-1]+nums[i]
        
#         for i in range(n-2,-1,-1):
#             suf[i]=suf[i+1]+nums[i]
        
#         res=max(res,pre[n-1])
#         mxsuf=suf[n-1]
#         for i in range(n-2,-1,-1):
#             res=max(res,pre[i]+mxsuf)
#             mxsuf=max(mxsuf,suf[i])
        
#         return res



# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         if max(nums)<=0: return max(nums)

#         mires=rsum=0
#         for i,x in enumerate(nums):
#             if rsum+x<0: rsum+=x
#             else: rsum=0
#             mires=min(mires,rsum)

#         mxres=rsum=0
#         for i,x in enumerate(nums):
#             if rsum+x>0: rsum+=x
#             else: rsum=0
#             mxres=max(mxres,rsum)
        
#         return max(mxres,sum(nums)-mires)


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums)<=0: return max(nums)

        tot=mires=mirsum=mxres=mxrsum=0
        for i,x in enumerate(nums):
            mirsum=min(mirsum+x,x)
            mires=min(mires,mirsum)
            mxrsum=max(mxrsum+x,x)
            mxres=max(mxres,mxrsum)
            tot+=x
        
        return max(mxres,tot-mires)