class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt=cand=0
        for x in nums:
            if cand==x: cnt+=1
            elif cnt!=0: cnt-=1
            else: cnt,cand=1,x
        
        return cand

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
        
#         cand,cnt=nums[0],1
#         for x in nums[1:]:
#             if cand==x: cnt+=1
#             else:
#                 cnt-=1
#                 if cnt==0: 
#                     cnt,cand=1,x
        
#         return cand