class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        mx=nmx=jumps=0
        for i in range(n-1):
            nmx=max(nmx,i+nums[i])
            if i==mx: 
                jumps+=1
                mx=nmx
        
        return jumps