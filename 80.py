# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
#         prev,pos=-inf,0
#         for x in nums:
#             if prev!=x: prev,cnt=x,1
#             else: cnt+=1
#             if cnt<=2: nums[pos]=x;pos+=1
#         return pos


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n,pos=len(nums),2
        for i in range(2,n):
            if nums[pos-2]!=nums[i]:
                nums[pos]=nums[i]
                pos+=1
        return pos
