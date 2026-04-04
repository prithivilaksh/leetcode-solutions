# ## TLE
# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
#         n=len(nums)
#         l=uniq=res=0
#         cnt=defaultdict(int)
#         for r,x in enumerate(nums):
#             cnt[x]+=1
#             if cnt[x]==1: uniq+=1
#             if uniq==k:
#                 nr=r+1
#                 while nr<n and nums[nr] in cnt: nr+=1
#                 nr-=1
#                 while uniq==k:
#                     res+=nr-r+1
#                     cnt[nums[l]]-=1
#                     if cnt[nums[l]]==0: 
#                         del cnt[nums[l]]
#                         uniq-=1
#                     l+=1
#         return res

# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
#         n=len(nums)
#         l=uniq=res=nr=0
#         cnt=defaultdict(int)
#         for r,x in enumerate(nums):
#             cnt[x]+=1
#             if cnt[x]==1: uniq+=1
#             if uniq==k:
#                 nr=max(nr,r+1)
#                 while nr<n and nums[nr] in cnt: nr+=1
#                 nr-=1
#                 while uniq==k:
#                     res+=nr-r+1
#                     cnt[nums[l]]-=1
#                     if cnt[nums[l]]==0: 
#                         del cnt[nums[l]]
#                         uniq-=1
#                     l+=1
#         return res

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        l=res=nr=0
        cnt=defaultdict(int)
        for r,x in enumerate(nums):
            cnt[x]+=1
            if len(cnt)==k:
                nr=max(nr,r+1)
                while nr<n and nums[nr] in cnt: nr+=1
                nr-=1
                while len(cnt)==k:
                    res+=nr-r+1
                    cnt[nums[l]]-=1
                    if cnt[nums[l]]==0: del cnt[nums[l]]
                    l+=1
        return res


# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
#         def atmostK(k):
#             cnt=defaultdict(int)
#             res=l=0
#             for r,x in enumerate(nums):
#                 cnt[x]+=1
#                 while len(cnt)>k:
#                     cnt[nums[l]]-=1
#                     if cnt[nums[l]]==0: del cnt[nums[l]]
#                     l+=1
#                 res+=r-l+1
#             return res
#         return atmostK(k)-atmostK(k-1)

            