# class Solution:
#     def minCostII(self, costs: List[List[int]]) -> int:

#         n,k=len(costs),len(costs[0])
#         @cache
#         def dp(pos,prev):
#             if pos==n: return 0
#             res=float("inf")
#             for i in range(k):
#                 if i==prev: continue
#                 res=min(res,costs[pos][i]+dp(pos+1,i))
#             return res
#         return dp(0,-1)
                
from typing import List
from math import inf
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        n,k=len(costs),len(costs[0])
        dp=[[inf]*k for _ in range(n+1)]
        dp[n]=[0]*k
        
        for pos in range(n-1,-1,-1):
            for prev in range(k):
                for i in range(k):
                    if i==prev: continue
                    dp[pos][prev]=min(dp[pos][prev],costs[pos][i]+dp[pos+1][i])
        
        return min(dp[0])
                

if __name__=="__main__":
    print(Solution().minCostII([[1,5,3],[2,9,4]]))
    print(Solution().minCostII([[1,3],[2,4]]))