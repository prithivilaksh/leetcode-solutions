# class Solution:
#     def getKth(self, lo: int, hi: int, k: int) -> int:
        
#         @cache
#         def dp(i):
#             if i==1: return 0
#             if i%2==0: return 1+dp(i//2)
#             return 1+dp(3*i+1)
        
#         return sorted(range(lo,hi+1),key=lambda x: dp(x))[k-1]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def dp(i):
            if i==1: return 0
            if i%2==0: return 1+dp(i//2)
            return 1+dp(3*i+1)
        
        return sorted(range(lo,hi+1),key=dp)[k-1]

# class Solution:
#     def getKth(self, lo: int, hi: int, k: int) -> int:
        
#         @cache
#         def dp(i):
#             if i==1: return 0
#             if i%2==0: return 1+dp(i//2)
#             return 1+dp(3*i+1)
        
#         return heapq.nsmallest(k,range(lo,hi+1),key=dp)[-1]

# class Solution:
#     def getKth(self, lo: int, hi: int, k: int) -> int:
        
#         @cache
#         def dp(i):
#             if i==1: return 0
#             if i%2==0: return 1+dp(i//2)
#             return 1+dp(3*i+1)
        
#         a=[(dp(i),i) for i in range(lo,hi+1)]
#         a.sort()
#         return a[k-1][1]