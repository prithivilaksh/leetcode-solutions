# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         @cache
#         def helper(amt):
#             res=100000
#             for x in coins:
#                 if amt>=x:
#                     res=min(res,1+helper(amt-x))
#             return 0 if amt==0 else res

#         res=helper(amt)
#         return res if res!=100000 else -1

class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        
        dp=[100000]*(amt+1)
        dp[0]=0
        for i in range(amt+1):
            for j in coins:
                if i>=j:
                    dp[i]=min(dp[i],1+dp[i-j])
        
        return dp[amt] if dp[amt]!=100000 else -1
