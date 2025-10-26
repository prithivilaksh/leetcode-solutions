# class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:

#         n=len(costs)

#         @cache
#         def dp(pos,pcol=-1):
#             if pos==n: return 0
#             res=inf
#             for i in range(3):
#                 if i==pcol: continue
#                 res=min(res,costs[pos][i]+dp(pos+1,i))
#             return res

#         return dp(0)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        n=len(costs)

        dp=[inf]*3

        for i in range(n-1,-1,-1):
            r=costs[i][0]+min(dp[1],dp[2])
            g=costs[i][1]+min(dp[0],dp[2])
            b=costs[i][2]+min(dp[0],dp[1])
            dp=[r,g,b]
        
        return min(dp)