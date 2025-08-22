#TLE
# class Solution:
#     def canReach(self, s: str, mi: int, mx: int) -> bool:
#         if s[-1]=="1": return False
        
#         n=len(s)
#         @cache
#         def dp(i):
#             if i==n-1: return True
#             for j in range(i+mi,min(i+mx+1,n)):
#                 if s[j]=="0" and dp(j): return True
#             return False
        
#         return dp(0)
        
        
class Solution:
    def canReach(self, s: str, mi: int, mx: int) -> bool:
        if s[-1]=="1": return False

        n=len(s)
        dq=deque([0])
        for j in range(1,n):
            if s[j]=="1" : continue
            l,r=j-mx,j-mi
            while dq and dq[0]<l: dq.popleft()
            if not dq: return False
            if dq[0]<=r : dq.append(j)
        
        return dq[-1]==n-1

# class Solution:
#     def canReach(self, s, mi, mx):
#         n,cnt=len(s),0
#         dp=[1]+[0]*(n-1)
#         for i in range(1, n):
#             if i >= mx-1: cnt -= dp[i - mx - 1]
#             if i >= mi: cnt += dp[i - mi]
#             dp[i] = cnt>0 and s[i]=="0"
#         return dp[-1]

# class Solution:
#     def canReach(self, s: str, mi: int, mx: int) -> bool:
       
#         if s[-1]=="1": return False
#         n=len(s)
#         q=deque([0])
#         mxVis=0
#         while q:
#             i=q.popleft()
#             for j in range(max(i+mi,mxVis+1),min(i+mx+1,n)):
#                 if s[j]=="0":
#                     if j==n-1: return True
#                     q.append(j)
#             mxVis=i+mx
#         return False

        