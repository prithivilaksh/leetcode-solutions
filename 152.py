# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
        
#         @cache
#         def helper(pos,isMx=True):
#             if pos==n-1: return nums[pos]

#             if isMx:
#                 if nums[pos]<0: return max(nums[pos],nums[pos]*helper(pos+1,False))
#                 else: return max(nums[pos],nums[pos]*helper(pos+1,True))
#             else:
#                 if nums[pos]<0: return min(nums[pos],nums[pos]*helper(pos+1,True))
#                 else: return min(nums[pos],nums[pos]*helper(pos+1,False))

#         n=len(nums)
#         res=-inf
#         for i in range(n):
#             res=max(res,helper(i))

#         return res

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         dp=[[0,0] for i in range(n)]
#         dp[n-1][0]=dp[n-1][1]=res=nums[n-1]
    
#         for i in range(n-2,-1,-1):
#             dp[i][0]=min(nums[i],nums[i]*dp[i+1][nums[i]<0])
#             dp[i][1]=max(nums[i],nums[i]*dp[i+1][nums[i]>0])
#             res=max(res,dp[i][1])
        
#         return res
        
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
        
#         # Observation:
#         # 1) the array can have 0 and -ve numbers
#         # 2) If there are no zeros and for any subarray nums[i:j]
#         #     - if p[i,j]>0 or (Vice versa)
#         #         if i-1 or j+1 is +ve, or both are negative include them.
#         #         if one is positive, include that -> it could be either prefix or suffix product
#         # 3) if there are zeros, reset to 1

#         def helper(nums):
#             res,p=-inf,1
#             for x in nums:
#                 p*=x
#                 res=max(res,p)
#                 if p==0:p=1
#             return res
#         return max(helper(nums),helper(nums[::-1]))

class Solution:
    def maxProduct(self, A):
                
        # Observation:
        # 1) the array can have 0 and -ve numbers
        # 2) If there are no zeros and for any subarray nums[i:j]
        #     - if p[i,j]>0 or (Vice versa)
        #         if i-1 or j+1 is +ve, or both are negative include them.
        #         if one is positive, include that -> max product could be either prefix or suffix product
        # 3) if there are zeros, reset to 1
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)