# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
        
#         cnt,l,r=defaultdict(int),defaultdict(int),defaultdict(int)
#         for i,x in enumerate(nums):
#             cnt[x]+=1
#             r[x]=i
#             if x not in l: l[x]=i
#         deg=max(cnt.values())
#         res=len(nums)
#         for x,cnt in cnt.items():
#             if cnt==deg:
#                 res=min(res,r[x]-l[x]+1)
#         return res

# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
        
#         n2i=defaultdict(list)
#         for i,x in enumerate(nums): n2i[x].append(i)

#         f=l=0
#         for x,inds in n2i.items():
#             if len(inds)>f:
#                 f,l=len(inds),inds[-1]-inds[0]+1
#             elif len(inds)==f:
#                 l=min(l,inds[-1]-inds[0]+1)
#         return l

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count, res, degree = defaultdict(int),defaultdict(int), 0, 0
        for i, x in enumerate(nums):
            if x not in first: first[x]=i
            count[x]+=1
            if count[x] > degree:
                degree = count[x]
                res = i - first[x] + 1
            elif count[x] == degree:
                res = min(res, i - first[x] + 1)
        return res