# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         mi,res=inf,0
#         for x in prices:
#             res=max(res,x-mi)
#             mi=min(mi,x)
#         return res

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         mi,res=inf,0
#         for x in prices:
#             if x-mi>res: res=x-mi
#             if x<mi: mi=x
#         return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mi,res=inf,0
        for x in prices:
            if x<mi: mi=x
            else: res=max(res,x-mi)
        return res