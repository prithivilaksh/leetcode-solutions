# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
#         @cache
#         def dp(pos):
#             if pos==n: return 0
#             res=inf

#             res=min(res,costs[0]+dp(pos+1))

#             pos7=bisect_right(days,days[pos]+6,lo=pos)
#             res=min(res,costs[1]+dp(pos7))

#             pos30=bisect_right(days,days[pos]+29,lo=pos)
#             res=min(res,costs[2]+dp(pos30))

#             return res
#         n=len(days)
#         return dp(0)

# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
#         @cache
#         def dp(pos):
#             if pos==n: return 0
#             pos7=bisect_right(days,days[pos]+6,lo=pos+1)
#             pos30=bisect_right(days,days[pos]+29,lo=pos+1)
#             return min(costs[0]+dp(pos+1),costs[1]+dp(pos7),costs[2]+dp(pos30))
#         n=len(days)
#         return dp(0)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        cnt = 0
        for i in range(1, days[-1] + 1):
            if i < days[cnt]: dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
                cnt += 1
        return dp[-1]