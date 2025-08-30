# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         n=len(nums)
#         lr,rl,res=[1]*n,[1]*n,[1]*n

#         lr[0]=nums[0]
#         for i in range(1,n):
#             lr[i]=lr[i-1]*nums[i]
        
#         rl[n-1]=nums[n-1]
#         for i in range(n-2,-1,-1):
#             rl[i]=rl[i+1]*nums[i]
        
#         res[0]=rl[1]
#         res[n-1]=lr[n-2]
#         for i in range(1,n-1):
#             res[i]=lr[i-1]*rl[i+1]
        
#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        pre=suf=1
        res=[1]*n

        for i in range(n):
            res[i]*=pre
            pre*=nums[i]
        
        for i in range(n-1,-1,-1):
            res[i]*=suf
            suf*=nums[i]
        
        return res