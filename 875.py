# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
#         l,r=1,max(piles)

#         def check(k):
#             hrs=0
#             for x in piles:
#                 hrs+=ceil(x/k)
#                 if hrs>h: return False
#             return True

#         while l<r:
#             m=l+(r-l)//2
#             if check(m): r=m
#             else: l=m+1
#         return r

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r=1,max(piles)

        while l<r:
            m=l+(r-l)//2
            if sum(ceil(x/m) for x in piles)<=h: r=m
            else: l=m+1
        return r