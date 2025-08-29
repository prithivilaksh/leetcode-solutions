# class Solution:
#     def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        
#         sep=sorted(zip(s,e,p))
#         n,res=len(sep),0
#         dp=[0]*(n+1)

#         for i in range(n-1,-1,-1):
#             nxt=bisect_left(sep,(sep[i][1],0,0))
#             dp[i]=sep[i][2]
#             for j in range(nxt,n):
#                 if sep[nxt][1]<=sep[j][0]:break
#                 dp[i]=max(dp[i],sep[i][2]+dp[j])
#             res=max(res,dp[i])

#         return res
        
# class Solution:
#     def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        
#         sep=sorted(zip(s,e,p))
#         n=len(sep)
#         @cache
#         def dp(i):#max profit to the right of i (inclusive)
#             if i>=n: return 0
#             nxt=bisect_left(sep,(sep[i][1],0,0))
#             return max(sep[i][2]+dp(nxt),dp(i+1))
        
#         return dp(0)

# class Solution:
#     def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        
#         sep=sorted(zip(s,e,p))
#         n=len(sep)
#         @cache
#         def dp(i):#max profit to the right of i (inclusive)
#             if i>=n: return 0
#             nxt=bisect_left(sep,(sep[i][1],0,0),lo=i+1)
#             return max(sep[i][2]+dp(nxt),dp(i+1))
        
#         return dp(0)
        

class Solution:
    def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        
        sep=sorted(zip(s,e,p))
        n=len(sep)
        dp=[0]*(n+1)
        
        for i in range(n-1,-1,-1):
            _,e,p=sep[i]
            j=bisect_left(sep,(e,),lo=i+1,hi=n)
            dp[i]=max(p+dp[j],dp[i+1])
        
        return dp[0]
        

# class Solution:
#     def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        
#         n=len(s)
#         ind=sorted(range(n),key=lambda x:e[x])
#         dp,end=[0],[0]
#         for i in ind:
#             j=bisect_right(end,s[i])-1
#             if dp[-1]<dp[j]+p[i]:
#                 end.append(e[i])
#                 dp.append(dp[j]+p[i])
        
#         return dp[-1]
        