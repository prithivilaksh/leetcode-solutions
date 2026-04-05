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

# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:
        
#         res,nxt=0,1
#         for x in nums:
#             while nxt<x and nxt<=n: nxt+=nxt;res+=1
#             nxt+=x
#             if nxt>n: break
#         while nxt<=n: nxt+=nxt;res+=1
#         return res

# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:

#         res=upto=0
#         next=1
#         for x in nums:
#             while next<x and next<=n:
#                 res+=1
#                 upto+=next
#                 next=upto+1
#             if next>n: return res
#             upto+=x
#             next=upto+1

#         while next<=n:
#             res+=1
#             upto+=next
#             next=upto+1

#         return res

# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:

#         m=len(nums)
#         res=upto=i=0
#         next=1

#         while next<=n:
#             if i<m and nums[i]<=next:
#                 upto+=nums[i]
#                 next=upto+1
#                 i+=1
#             else:
#                 upto+=next
#                 next=upto+1
#                 res+=1
        
#         return res

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        m=len(nums)
        res=i=0
        next=1

        while next<=n:
            if i<m and nums[i]<=next:
                next+=nums[i]
                i+=1
            else:
                next+=next
                res+=1
                
        return res
