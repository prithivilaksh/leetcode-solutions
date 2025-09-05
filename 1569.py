# class Solution:
#     def numOfWays(self, nums: List[int]) -> int:
#         mod=10**9+7
#         def ways(nums):
#             n=len(nums)
#             if n<=2: return 1

#             root,left,right=nums[0],[],[]
#             for i in range(1,n):
#                 if nums[i]<root: left.append(nums[i])
#                 else: right.append(nums[i])
            
#             lways,rways=ways(left),ways(right)

#             return (comb(n-1,len(left))*lways*rways)%mod

#         return ways(nums)-1

class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        # observations:
        #     - if the len(nums)<=2 then there can be only 1 order as root will be first and the remaining element will be next
        #     - we can change the base condition to n<=1 as well
        #     - for any array nums, the root will always be nums[0]
        #     - we know the ways of left and right subtree (since it is the same sub problem)
        #     - we have totally n-1 positions to be filled from left and right subtree.
        #     - we can pick any combination of left or right to fill in the rem n-1 positions for each possible way as left is independent of right
        #     - ncr = nc(n-r)
        mod=10**9+7
        def ways(nums):
            n=len(nums)
            if n<=2: return 1

            root=nums[0]
            l=[x for x in nums if x<root]
            r=[x for x in nums if x>root]

            return (comb(n-1,len(l)) * ways(l) * ways(r)) % mod

        return (ways(nums)-1) % mod


        # 3

        # 12
        # 45

        # total 4
        # number of ways to place 1,2 in the same order in 4 poistions
        # 1 2 _ _
        # 1 _ 2 _
        # 1 _ _ 2
        # _ 1 2 _
        # _ 1 _ 2
        # _ _ 1 2


