# class Solution:
#     def minimumReplacement(self, nums: List[int]) -> int:
#         n,res=len(nums),0
#         nxt=nums[n-1]
#         for i in range(n-2,-1,-1):
#             if nums[i]<=nxt:nxt=nums[i]
#             else:
#                 k=ceil(nums[i]/nxt)
#                 nxt=nums[i]//k
#                 res+=k-1
#         return res

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        # observation/idea:
        #     1) we can only break an element => convert bigger to smaller (cannot convert small to big)
        #     2) we should break nums[i] if nums[i]>nums[i+1]. But if we break nums[i], then we may need to break nums[i-1] and so on.
        #     3) we cannot increase the last element so it is always fixed.
        #     4) based on 2) and 3) it would make sense to iterate from the end
        #     5) if nums[i]<=nxt, then no need to break nums[i]
        #     6) if nums[i]>nxt, we need to break nums[i] while making sure the following:
        #         a) number of operations is less
        #         b) the minimum number after breaking is as huge as possible
        #         c) the maximum number after breaking is <=nxt
        #     7) min number of elements after breaking, k = ceil(nums[i]/nxt)
        #     8) min number after breaking = nums[i]//k (distribute as evenly as possible)
        #     9) ops for breaking nums[i] = k-1


        n,res=len(nums),0
        nxt=nums[n-1]
        for x in nums[::-1]:
            if x<=nxt: nxt=x
            else:
                k=ceil(x/nxt)
                nxt=x//k
                res+=k-1
        return res

# class Solution:
#     def minimumReplacement(self, nums):
#         nxt,res = nums[-1],0
#         for x in reversed(nums):
#             k = ceil(x/nxt)
#             nxt = x // k
#             res += k - 1
#         return res