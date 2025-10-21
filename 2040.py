# class Solution:

#     def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         """
#         Find the kth smallest product from all possible nums1[i] * nums2[j] pairs.

#         Time Complexity: O(log(10^10) * m) where m = len(nums1)
#                         Binary search with O(m) counting per iteration
#         Space Complexity: O(m) for splitting nums1 into negative and non-negative parts
#         """
#         neg = [x for x in nums1 if x < 0]
#         pos = [x for x in nums1 if x >= 0 ]

#         def count_products_le(target):
#             """Count products <= target"""
#             count = 0
#             left, right = 0, len(nums2) - 1

#             # Choose order based on target sign for optimal two-pointer traversal
#             nums = neg[::-1] + pos if target >= 0 else neg + pos[::-1]

#             for num in nums:
#                 if num < 0:
#                     # Negative: find first nums2[j] where num * nums2[j] <= target
#                     while left < len(nums2) and num * nums2[left] > target:
#                         left += 1
#                     count += len(nums2) - left
#                 elif num == 0:
#                     # Zero: all products are 0
#                     if target >= 0:
#                         count += len(nums2)
#                 else:
#                     # num > 0
#                     # Positive: find last nums2[j] where num * nums2[j] <= target
#                     while right >= 0 and num * nums2[right] > target:
#                         right -= 1
#                     count += right + 1
#             return count


#         # Binary search on answer space
#         left, right = -10**10, 10**10

#         while left < right:
#             mid = (left + right) // 2
#             if count_products_le(mid) < k:
#                 left = mid + 1
#             else:
#                 right = mid

#         return left

# class Solution:
#     def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:
        

#         # idea/observation:
#         # 1) x<0 and y<0 => prd>0.
#         # 2) x<0 and y>0 => prd<0.
#         # 3) x>0 and y<0 => prd<0. x=5, prd=-20, y=-4 b=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
#         # 4) x>0 and y>0 => prd>0. x=5, prd=20, y=4 b=[-5,-4,-3,-2,-1,0,1,2,3,4,5]

#         def cntle(p):
#             cnt=0
#             for x in a:
#                 if x==0:
#                     if p>=0: cnt+=len(b)
#                     continue
#                 y=p/x
#                 if x>0: cnt+=bisect_right(b,floor(y))
#                 elif x<0: cnt+=len(b)-bisect_left(b,ceil(y))

#             return cnt

#         l,r,res=-10**10,10**10,None
#         while l<=r:
#             m=l+(r-l)//2
#             if cntle(m)>=k: res=m;r=m-1
#             else: l=m+1
        
#         return res


class Solution:
    def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:

        # idea/observation:
        # count number of products <= given product and do binary search
        # 1) x<0 and y<0 => prd>0. x=-5, prd=18, y=-3.xx, b=[-5,-4,|-3,-2,-1,0,1,2,3,4,5]
        # 2) x<0 and y>0 => prd<0. x=-5, prd=-18, y=3.xx, b=[-5,-4,-3,-2,-1,0,1,2,3,|4,5]
        # 3) x>0 and y<0 => prd<0. x=5, prd=-18, y=-3.xx, b=[-5,-4|,-3,-2,-1,0,1,2,3,4,5]
        # 4) x>0 and y>0 => prd>0. x=5, prd=18, y=3.xx, b=[-5,-4,-3,-2,-1,0,1,2,3|,4,5]

        def cntle(p):
            cnt=0
            for x in a:
                if x==0 and p>=0: y=10**10
                elif x==0 and p<0: y=-10**10
                else: y=p/x

                if x>=0: cnt+=bisect_right(b,floor(y))
                elif x<0: cnt+=len(b)-bisect_left(b,ceil(y))

            return cnt

        l,r,res=-10**10,10**10,None
        while l<=r:
            m=l+(r-l)//2
            if cntle(m)>=k: res=m;r=m-1
            else: l=m+1
        
        return res

# ## TLE
# class Solution:
#     def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:

#         m,n=len(a),len(b)
#         vis,h=set(),[]

#         def add(i,j):
#             if (i,j) not in vis:
#                 vis.add((i,j))
#                 heappush(h,(a[i]*b[j],i,j))
#         add(0,0)
#         add(0,n-1)
#         add(m-1,0)
#         add(m-1,n-1)

#         while k:
#             res,i,j=heappop(h)
#             k-=1
#             if i+1<m: add(i+1,j)
#             if i-1>=0: add(i-1,j)
#             if j+1<n: add(i,j+1)
#             if j-1>=0: add(i,j-1)

#         return res

