# class Solution:
#     def maxTwoEvents(self, events: List[List[int]]) -> int:
        
#         events.sort()
#         n,res=len(events),0
#         dp=[0]*(n+1)
#         for i in range(n-1,-1,-1):
#             _,end,val=events[i]
#             nxt=bisect_left(events,[end+1],lo=i+1)
#             res=max(res,val+dp[nxt])
#             dp[i]=max(val,dp[i+1])
#         return res

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        n,res,mx=len(events),0,0
        h=[]
        for s,e,v in events:
            while h and h[0][0]<s:
                oe,ov=heappop(h)
                mx=max(mx,ov)
            res=max(res,mx+v)
            heappush(h,(e,v))
        return res


    # 1,3,2   1,5,    4,5