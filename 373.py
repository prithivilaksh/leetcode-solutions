# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
#         m,n=len(nums1),len(nums2)
#         h,res,vis=[(nums1[0]+nums2[0],0,0)],[],set((0,0))
#         for _ in range(k):
#             _,i,j=heappop(h)
#             res.append([nums1[i],nums2[j]])
#             if i+1<m and (i+1,j) not in vis: 
#                 vis.add((i+1,j))
#                 heappush(h,(nums1[i+1]+nums2[j],i+1,j))
#             if j+1<n and (i,j+1) not in vis: 
#                 vis.add((i,j+1))
#                 heappush(h,(nums1[i]+nums2[j+1],i,j+1))
#         return res

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # # visualization
        #     j   0   1   2   3   4
        # i   
        # 0       0   1   3
        # 1       1   3
        # 2       2
        # 3
        # 4
        m,n=len(nums1),len(nums2)
        h,res=[(nums1[0]+nums2[0],0,0)],[]
        for _ in range(k):
            _,i,j=heappop(h)
            res.append([nums1[i],nums2[j]])
            if i==0 and j+1<n: heappush(h,(nums1[i]+nums2[j+1],i,j+1))
            if i+1<m: heappush(h,(nums1[i+1]+nums2[j],i+1,j))
        return res


# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
#         m,n=len(nums1),len(nums2)
#         h,res=[],[]
#         for j in range(n): heappush(h,(nums1[0]+nums2[j],0,j))
#         for _ in range(k):
#             _,i,j=heappop(h)
#             res.append([nums1[i],nums2[j]])
#             if i+1<m: heappush(h,(nums1[i+1]+nums2[j],i+1,j))
#         return res