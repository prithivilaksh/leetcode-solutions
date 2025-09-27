# class Solution:
#     def climbStairs(self, n: int, costs: List[int]) -> int:
#         n+=1
#         costs=[0]+costs

#         @cache
#         def dp(i):
#             if i==n-1: return costs[i]
#             if i>=n: return inf
            
#             res=costs[i]+min(1+dp(i+1),4+dp(i+2),9+dp(i+3))
#             return res

#         return dp(0)

# class Solution:
#     def climbStairs(self, n: int, costs: List[int]) -> int:
#         n+=1
#         costs=[0]+costs
#         dp=[0]*n
#         dp[n-1]=costs[n-1]
#         for i in range(n-2,-1,-1):
#             mi=inf
#             if i+1<=n-1: mi=min(mi,1+dp[i+1])
#             if i+2<=n-1: mi=min(mi,4+dp[i+2])
#             if i+3<=n-1: mi=min(mi,9+dp[i+3])
#             dp[i]=costs[i]+mi

#         return dp[0]


# class Solution:
#     def climbStairs(self, n: int, costs: List[int]) -> int:
#         n+=1
#         costs=[0]+costs
#         dis=[inf]*n
#         h=[(0,0)]

#         while h:
#             d,i=heappop(h)
#             if i==n-1: return d
#             if d>dis[i]: continue
#             for j in range(1,4):
#                 if i+j<=n-1:
#                     jd=d+(j**2)+costs[i+j]
#                     if jd<dis[i+j]: 
#                         dis[i+j]=jd
#                         heappush(h,(jd,i+j))
        
#         return -1

class Solution:
    def climbStairs(self, n: int, dp: List[int]) -> int:
        n+=1
        dp=[0]+dp
        for i in range(n-2,-1,-1):
            mi=inf
            if i+1<=n-1: mi=min(mi,1+dp[i+1])
            if i+2<=n-1: mi=min(mi,4+dp[i+2])
            if i+3<=n-1: mi=min(mi,9+dp[i+3])
            dp[i]=dp[i]+mi

        return dp[0]
        