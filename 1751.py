# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
        
#         events.sort()
#         n=len(events)

#         @cache
#         def dp(i,k):
#             if i==n or k==0: return 0
#             j=bisect_left(events,events[i][1]+1,lo=i+1,key=lambda x:x[0])
#             a=events[i][2]+dp(j,k-1)
#             b=dp(i+1,k)
#             return max(a,b)

#         return dp(0,k)

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()
        n=len(events)
        dp=[[0]*(k+1) for i in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(1,k+1):
                nxt=bisect_left(events,events[i][1]+1,lo=i+1,key=lambda x:x[0])
                dp[i][j]=max(events[i][2]+dp[nxt][j-1],dp[i+1][j])

        return dp[0][k]