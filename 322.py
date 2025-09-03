# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         @cache
#         def dp(amt):
#             if amt==0: return 0
#             res=inf
#             for c in coins:
#                 if amt>=c:
#                     res=min(res,1+dp(amt-c))
#             return res
        
#         res=dp(amt)
#         return res if res!=inf else -1

class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:

        dp=[0]+[inf]*amt
        for i in range(amt+1):
            for j in coins:
                if i>=j:
                    dp[i]=min(dp[i],dp[i-j]+1)

        return dp[amt] if dp[amt]!=inf else -1
