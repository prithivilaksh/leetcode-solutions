class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:

        # observation:
        # for all i the result can be either of the below
        # 1) max from the left inclusive -> lmax
        # 2) res[i+1] if lmax > rmin(exclusive) | the res[i+1] includes lmax for i+1
        
        n=len(nums)
        lmax,rmin,res=[0]*n,[0]*n,[0]*n

        lmax[0]=nums[0]
        for i in range(1,n):
            lmax[i]=max(lmax[i-1],nums[i])
        
        rmin[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            rmin[i]=min(rmin[i+1],nums[i])
        
        res[n-1]=lmax[n-1]
        for i in range(n-2,-1,-1):
            if lmax[i]>rmin[i+1]: res[i]=res[i+1]
            else: res[i]=lmax[i]
        
        return res
        
    