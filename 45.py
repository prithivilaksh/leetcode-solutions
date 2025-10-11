# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n=len(nums)
#         mx=nmx=jumps=0
#         for i in range(n-1):
#             nmx=max(nmx,i+nums[i])
#             if i==mx: 
#                 jumps+=1
#                 mx=nmx
        
#         return jumps


## Naive DP TLE
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n=len(nums)
#         def dp(i):
#             if i>=n-1: return 0
#             res=inf
#             for k in range(i+1,i+nums[i]+1):
#                 res=min(res,1+dp(k))
#             return res
#         return dp(0)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        res=cmax=gmax=0
        for i in range(n-1):
            cmax=max(cmax,i+nums[i])
            if i==gmax:
                gmax=cmax
                res+=1
        return res



# class Solution:
#     def jump(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         steps=[inf]*n
#         steps[0]=mxvis=0

#         for i in range(n-1):
#             l,r=max(i,mxvis+1),min(n-1,i+nums[i])
#             for k in range(l,r+1):
#                 steps[k]=steps[i]+1
#             mxvis=max(mxvis,r)

#         return steps[n-1]


# class Solution:
#     def jump(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         steps=[inf]*n
#         steps[0]=mxvis=0

#         for i in range(n-1):
#             l,r=mxvis+1,min(n-1,i+nums[i])
#             for k in range(l,r+1):
#                 steps[k]=steps[i]+1
#             mxvis=max(mxvis,r)

#         return steps[n-1]
