# class Solution:
#     def minArrivalsToDiscard(self, arr: List[int], w: int, m: int) -> int:

#         cnt=defaultdict(int)
#         l=res=0
#         for r,t in enumerate(arr):
#             if l<=r-w: cnt[arr[l]]-=1;l+=1
#             cnt[t]+=1
#             if cnt[t]==m+1:
#                 cnt[t]-=1
#                 arr[r]=-1
#                 res+=1
#         return res
            
# class Solution:
#     def minArrivalsToDiscard(self, arr: List[int], w: int, m: int) -> int:

#         cnt=defaultdict(int)
#         res=0
#         for r,t in enumerate(arr):
#             if r-w>=0: cnt[arr[r-w]]-=1
#             cnt[t]+=1
#             if cnt[t]==m+1:
#                 cnt[t]-=1
#                 arr[r]=-1
#                 res+=1
#         return res


class Solution:
    def minArrivalsToDiscard(self, arr: List[int], w: int, m: int) -> int:

        cnt=defaultdict(int)
        res=0
        for r,t in enumerate(arr):
            if r-w>=0: cnt[arr[r-w]]-=1
            if cnt[t]==m:
                arr[r]=-1
                res+=1
            else: cnt[t]+=1
        return res
            