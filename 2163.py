# class Solution:
#     def minimumDifference(self, nums: List[int]) -> int:
#         n=len(nums)//3
#         csum,h=0,[]
#         for i in range(n):
#             csum+=nums[i]
#             heappush(h,-nums[i])
        
#         left=[csum]
#         for i in range(n,2*n):
#             heappush(h,-nums[i])
#             csum+=nums[i]
#             csum-=-heappop(h)
#             left.append(csum)
        
#         csum,h=0,[]
#         for i in range(2*n,3*n):
#             csum+=nums[i]
#             heappush(h,nums[i])
        
#         right=[csum]
#         for i in range(2*n-1,n-1,-1):
#             heappush(h,nums[i])
#             csum+=nums[i]
#             csum-=heappop(h)
#             right.append(csum)
#         right=right[::-1]

#         return min(l-r for l,r in zip(left,right))


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        
        csum,h=sum(nums[:n]),[-x for x in nums[:n]]
        left=[csum]
        heapify(h)
        for i in range(n,2*n):
            csum+=nums[i]
            csum-=-heappushpop(h,-nums[i])
            left.append(csum)
        
        csum,h=sum(nums[2*n:3*n]),[x for x in nums[2*n:3*n]]
        right=[csum]
        heapify(h)
        for i in range(2*n-1,n-1,-1):
            csum+=nums[i]
            csum-=heappushpop(h,nums[i])
            right.append(csum)

        return min(l-r for l,r in zip(left,right[::-1]))

            