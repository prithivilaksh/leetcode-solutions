# class Solution:
#     def countNicePairs(self, nums: List[int]) -> int:
        
#         #idea
#         # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
#         # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        
#         cnt=defaultdict(int)

#         def rev(x):
#             res=0
#             while x:
#                 res=res*10+x%10
#                 x//=10
#             return res

#         res,mod=0,10**9+7
#         for x in nums:
#             rx=rev(x)
#             res=(res+cnt[x-rx])%mod
#             cnt[x-rx]+=1
#         return res


# class Solution:
#     def countNicePairs(self, nums: List[int]) -> int:
        
#         #idea
#         # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
#         # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        
#         cnt=defaultdict(int)
#         res,mod=0,10**9+7
#         for x in nums:
#             rx=int(str(x)[::-1])
#             res=(res+cnt[x-rx])%mod
#             cnt[x-rx]+=1
#         return res

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        #idea
        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        
        cnt=defaultdict(int)
        res,mod=0,10**9+7
        for x in nums:
            rx=int(str(x)[::-1])
            cnt[x-rx]+=1
        for c in cnt.values():
            if c>1: res+=comb(c,2)%mod
        return res%mod
