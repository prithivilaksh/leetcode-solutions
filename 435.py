# class Solution:
#     def eraseOverlapIntervals(self, ints: List[List[int]]) -> int:
#         ints.sort(key=lambda x:x[0])
#         res=0
#         ps,pe=ints[0]
#         for a,b in ints[1:]:
#             if pe>a: res+=1;pe=min(pe,b)
#             else: pe=b
#         return res

class Solution:
    def eraseOverlapIntervals(self, ints: List[List[int]]) -> int:
        ints.sort(key=lambda x:x[1])
        res=0
        ps,pe=ints[0]
        for a,b in ints[1:]:
            if pe>a: res+=1
            else: pe=b
        return res