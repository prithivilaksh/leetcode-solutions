# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:
        
#         next,cnt,i,m=1,0,0,len(nums)
#         while True:
#             while i<m and nums[i]<=next:
#                 next+=nums[i]
#                 i+=1
#             if next>n: break
#             next+=next
#             cnt+=1
#         return cnt

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        res,nxt=0,1
        for x in nums:
            while nxt<x and nxt<=n: nxt+=nxt;res+=1
            nxt+=x
            if nxt>n: break
        while nxt<=n: nxt+=nxt;res+=1
        return res
