# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         bl=max(nums).bit_length()
#         mx=1<<bl

#         dp=[0]*mx
#         for x in nums:dp[x]=x
#         for i in range(mx):
#             if dp[i]: continue
#             for k in range(bl):
#                 if (i>>k)&1:
#                     j=i&~(1<<k)
#                     # j=i^(1<<k)
#                     if dp[j]>dp[i]:dp[i]=dp[j]
#         tmp=res=0
#         for x in nums:
#             tmp=x*dp[~x]
#             if tmp>res:res=tmp     
#         return res

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Observation:
        #     -for any number say 100101, it can be multiplied with its complement or complement's subset
        #     - eg 100101 complement is 011010 -> no intersection of set bits
        #     - also 100101 complement's subset is 011000 -> no intersection of set bits
        #     - for every number, bit by bit, update its state with the maximum values of its subset
        #     - in the above step we would have updated all the parents such that we only need to check x * ~x state as the complement's state contains all of its subsets state

        bl=max(nums).bit_length()
        mx=1<<bl

        dp=[0]*mx
        for x in nums:dp[x]=x
        
        for k in range(bl):
            for i in range(mx):
                if (i>>k)&1:
                    j=i^(1<<k) #j=i&~(1<<k)
                    if dp[j]>dp[i]:dp[i]=dp[j]
        tmp=res=0
        for x in nums:
            tmp=x*dp[~x]
            if tmp>res:res=tmp     
        return res

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:



#         bl=max(nums).bit_length()
#         mx=1<<bl

#         dp=[-1]*mx
#         for x in nums:dp[x]=x
        
#         for k in range(bl):
#             mask=1<<k
#             for i in range(mx):
#                 if i&mask:
#                     j=i^mask
#                     if dp[j]>dp[i]:dp[i]=dp[j]
#         tmp=res=0
#         for x in nums:
#             if dp[~x]!=-1:
#                 tmp=x*dp[~x]
#                 if tmp>res:res=tmp     
#         return res