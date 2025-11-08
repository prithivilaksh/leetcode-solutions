# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, t: int) -> int:
#         @cache
#         def dp(pos,pc,rem):
#             if pos==m: return 0 if rem==0 else inf

#             if houses[pos]!=0: return dp(pos+1,houses[pos],rem-(pc!=houses[pos]))

#             res=inf
#             for j in range(n):
#                 res=min(res,cost[pos][j]+dp(pos+1,j+1,rem-(pc!=j+1)))
            
#             return res

#         res=dp(0,-1,t)
#         return -1 if res==inf else res

# class Solution:
#     def minCost(self, h: List[int], cost: List[List[int]], m: int, n: int, t: int) -> int:
#         @cache
#         def dp(i,pc,rem):
#             if m-i<rem: return inf
#             if i==m: return 0 if rem==0 else inf

#             if h[i]!=0: return dp(i+1,h[i],rem-(pc!=h[i]))

#             res=inf
#             for j in range(n):
#                 if cost[i][j]<res:
#                     res=min(res,cost[i][j]+dp(i+1,j+1,rem-(pc!=j+1)))
            
#             return res

#         res=dp(0,-1,t)
#         return -1 if res==inf else res


class Solution:
    def minCost(self, h: List[int], cost: List[List[int]], m: int, n: int, t: int) -> int:
        @cache
        def dp(i,pc,rem):
            if m-i<rem: return inf
            
            if i==m: return 0 if rem==0 else inf

            if h[i]!=0: return dp(i+1,h[i],rem-(pc!=h[i]))
            
            return min(cost[i][j]+dp(i+1,j+1,rem-(pc!=j+1)) for j in range(n))

        res=dp(0,-1,t)
        return -1 if res==inf else res