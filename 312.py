class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums=[1]+nums+[1]
        n=len(nums)

        @cache
        def helper(i,j):
            res=0
            for k in range(i,j+1):
                left=helper(i,k-1)
                mid=nums[i-1]*nums[k]*nums[j+1]
                right=helper(k+1,j)
                res=max(res,left+mid+right)
            return res
        return helper(1,n-2)


        