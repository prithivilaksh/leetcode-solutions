# class Solution:
#     def perfectPairs(self, nums: List[int]) -> int:

#         n=len(nums)
#         nums = [abs(x) for x in nums]
#         nums.sort()
#         res=0
#         for i in range(n):
#             lo = bisect_left(nums, (nums[i] + 1) // 2)
#             hi = bisect_right(nums, nums[i] * 2) - 1
#             res += hi - lo
#         return res // 2 

# class Solution:
#     def perfectPairs(self, nums: List[int]) -> int:
#         nums = [abs(x) for x in nums]
#         nums.sort()
#         n = len(nums)
#         count = 0
#         left = 0
#         for right in range(n):
#             while left < right and 2*nums[left]<nums[right]:
#                 left += 1
#             count += right - left
#         return count


# class Solution:
#     def perfectPairs(self, nums: List[int]) -> int:

#         # observation:
#         # min(|a-b|,|a+b|) = | |a|-|b| | <= min(|a|,|b|)
#         # max(|a-b|,|a+b|) = | |a|+|b| | >= max(|a|,|b|)

#         # when |a|<|b|:
#         #     | |a|-|b| |<=|a|
#         #     |b|-|a|<=|a|
#         #     |b|<=2*|a|

#         #     |a|+|b|>=|b|
#         #     |a|>=0 always True
        
#         # when |a|>|b|
#         #     |a|-|b|<=|b|
#         #     |a|<=2*|b|

#         #     |a|+|b|>=|b|
#         #     |a|>=0 always True

#         nums=sorted([abs(x) for x in nums])
#         l,n,res=0,len(nums),0
#         for r in range(n):
#             # 2*l>=r
#             l=bisect_left(nums,ceil(nums[r]/2))
#             res+=r-l
#         return res



class Solution:
    def perfectPairs(self, nums: List[int]) -> int:

        # observation:
        # min(|a-b|,|a+b|) = | |a|-|b| | <= min(|a|,|b|)
        # max(|a-b|,|a+b|) = | |a|+|b| | >= max(|a|,|b|)

        # when |a|<|b|:
        #     | |a|-|b| |<=|a|
        #     |b|-|a|<=|a|
        #     |b|<=2*|a|

        #     |a|+|b|>=|b|
        #     |a|>=0 always True
        
        # when |a|>|b|
        #     |a|-|b|<=|b|
        #     |a|<=2*|b|

        #     |a|+|b|>=|b|
        #     |a|>=0 always True

        nums=sorted([abs(x) for x in nums])
        l,n,res=0,len(nums),0
        for r in range(n):
            while l<r and 2*nums[l]<nums[r]:l+=1
            res+=r-l
        return res

        



       



























