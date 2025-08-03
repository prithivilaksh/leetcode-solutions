# class Solution:
#     def isTrionic(self, nums: List[int]) -> bool:

#         n=len(nums)
#         i=cnt=0
#         while i+1<n and nums[i]<nums[i+1]:i+=1;cnt+=1
#         if cnt==0: return False
        
#         cnt=0
#         while i+1<n and nums[i]>nums[i+1]: i+=1;cnt+=1
#         if cnt==0: return False
        
#         cnt=0
#         while i+1<n and nums[i]<nums[i+1]:i+=1;cnt+=1
#         if cnt==0: return False

#         return i+1==n

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        n=len(nums)
        i,n=0,len(nums)
        def isNotSeq(sign):
            nonlocal i
            flag=True
            while i+1<n and nums[i]*sign<nums[i+1]*sign:i+=1;flag=False
            return flag
        
        if isNotSeq(1) or isNotSeq(-1) or isNotSeq(1):return False
        return i+1==n