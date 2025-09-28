# class Solution:
#     def splitArray(self, nums: List[int]) -> int:
        
#         i,n=0,len(nums)

#         while i+1<n and nums[i]<nums[i+1]: i+=1
#         ind1=ind2=i
#         if i+1<n and nums[i]==nums[i+1]:ind2=i;i+=1
#         while i+1<n and nums[i]>nums[i+1]: i+=1

#         if i+1!=n: return -1
#         if ind1==ind2:
#             ind=ind1
#             first=abs(sum(nums[:ind])-sum(nums[ind:]))
#             second=abs(sum(nums[:ind+1])-sum(nums[ind+1:]))
#             if ind==n-1: return first
#             elif ind==0: return second
#             return min(first,second)
#         return abs(sum(nums[:ind2])-sum(nums[ind2:]))
            
class Solution:
    def splitArray(self, nums: List[int]) -> int:             
        maximum = nums.index(max(nums))

        for i in range(maximum):
            if nums[i] >= nums[i + 1]:
                return -1

        for i in range(maximum + 1, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                return -1

        diff1 = abs(sum(nums[:maximum]) - sum(nums[maximum:]))
        diff2 = abs(sum(nums[:maximum + 1]) - sum(nums[maximum + 1:]))
        return min(diff1, diff2)

        