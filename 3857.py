# class Solution:
#     @cache
#     def minCost(self, n: int) -> int:
#         if n<=2: return n-1

#         res=inf
#         for i in range(1,n//2 +1):
#             res=min(res,i*(n-i)+self.minCost(i)+self.minCost(n-i))
#         return res

# class Solution:
#     @cache
#     def minCost(self, n: int) -> int:
#         if n<=2: return n-1
#         a=n//2
#         b=n-a
#         return a*b+self.minCost(a)+self.minCost(b)


class Solution:
    def minCost(self, n: int) -> int:
        return n*(n-1)//2