# class Solution:
#     def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

#         cnt,res=defaultdict(int),0
#         for x in arr: cnt[x]+=1

#         for c in sorted(cnt.values()):
#             if k>=c:k-=c
#             else: res+=1
#         return res

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        cnt,res=defaultdict(int),0
        for x in arr: cnt[x]+=1

        for i,c in enumerate(sorted(cnt.values())):
            k-=c
            if k<0: return len(cnt)-i
        return 0