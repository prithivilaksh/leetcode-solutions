# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         l=csum=res=0
#         for r,x in enumerate(nums):
#             csum+=x
#             while (r-l+1)*x-csum>k:
#                 csum-=nums[l]
#                 l+=1
#             res=max(res,r-l+1)
#         return res

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=csum=res=0
        for r,x in enumerate(nums):
            csum+=x
            if (r-l+1)*x-csum>k:
                csum-=nums[l]
                l+=1
        return r-l+1

# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         nums.sort()
#         pre=[nums[0]]
#         for x in nums[1:]: pre.append(pre[-1]+x)

#         def bs(i):
#             x=nums[i]
#             l,r=0,i
#             while l<r:
#                 m=l+(r-l)//2
#                 wsum=pre[i]-pre[m]+nums[m]
#                 wlen=i-m+1
#                 if wlen*x-wsum<=k: r=m
#                 else: l=m+1
#             return i-r+1

#         return max((bs(i) for i in range(n)),default=0)
