


# class Solution:
#     def minArraySum(self, nums: List[int], k: int) -> int:


#         # idea:
#         #     - if the sum[..i]%k == sum[..j]%k where i<j then sum[i+1..j]%k==0
#         #     - eg for k=3, nums=[4 1 2 5] , rem=[1 2 1 0]
        
#         n=len(nums)
#         remMinSum=[0]+[inf]*(k-1)
#         def helper(pos):
#             if pos==n: return 0
#             rsum=nums[pos]+helper(pos+1)
#             rem=rsum%k
#             remMinSum[rem]=min(remMinSum[rem],rsum)

#             return remMinSum[rem]

#         return helper(0)


# class Solution:
#     def minArraySum(self, nums: List[int], k: int) -> int:


#         # idea:
#         #     - if the sum[..i]%k == sum[..j]%k where i<j then sum[i+1..j]%k==0
#         #     - eg for k=3, nums=[4 1 2 5] , rem=[1 2 1 0]
        
#         n=len(nums)
        
#         def helper(pos):
#             if pos==n: return 0,[0]+[inf]*(k-1)
#             rsum,remMinSum=helper(pos+1)
#             rsum+=nums[pos]
#             rem=rsum%k
#             remMinSum[rem]=min(remMinSum[rem],rsum)

#             return remMinSum[rem],remMinSum

#         return helper(0)[0]
                
class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:


        # idea:
        #     - if the sum[..i]%k == sum[..j]%k where i<j then sum[i+1..j]%k==0
        #     - eg for k=3, nums=[4 1 2 5] , rem=[1 2 1 0]

        remMinSum=[0]+[inf]*(k-1)
        rsum=0
        for x in nums:
            rsum+=x
            rem=rsum%k
            rsum=remMinSum[rem]=min(remMinSum[rem],rsum)
        
        return rsum





















        




















        