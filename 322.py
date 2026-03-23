# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         coins.sort(reverse=True)
#         n=len(coins)
#         @cache
#         def dp(pos,amt):
#             if amt==0: return 0
#             if pos==n: return inf
            
#             res=dp(pos+1,amt)
#             if coins[pos]<=amt: res=min(res,1+dp(pos,amt-coins[pos]))
#             return res
        
#         res=dp(0,amt)
#         return -1 if res==inf else res

# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         # coins.sort(reverse=True)
#         n=len(coins)
#         @cache
#         def dp(pos,amt):
#             if amt==0: return 0
#             if pos==n: return inf
            
#             res=dp(pos+1,amt)
#             if coins[pos]<=amt: res=min(res,1+dp(pos,amt-coins[pos]))
#             return res
        
#         res=dp(0,amt)
#         return -1 if res==inf else res

# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         m,n=amt+1,len(coins)
#         dp=[[inf]*(n+1) for _ in range(amt+1)]
#         for j in range(n+1): dp[0][j]=0

#         for i in range(m):
#             for j in range(n-1,-1,-1):
#                 dp[i][j]=dp[i][j+1]
#                 if coins[j]<=i: dp[i][j]=min(dp[i][j],1+dp[i-coins[j]][j])
        
#         return -1 if dp[amt][0]==inf else dp[amt][0]

# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         m,n=amt+1,len(coins)
#         dp=[inf]*(amt+1)
#         dp[0]=0

#         for i in range(m):
#             for j in range(n-1,-1,-1):
#                 if coins[j]<=i: 
#                     dp[i]=min(dp[i],1+dp[i-coins[j]])

#         return -1 if dp[amt]==inf else dp[amt]

# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         m,n=amt+1,len(coins)
#         dp=[inf]*(amt+1)
#         dp[0]=0

#         for i in range(m):
#             for j in range(n):
#                 if coins[j]<=i: 
#                     dp[i]=min(dp[i],1+dp[i-coins[j]])

#         return -1 if dp[amt]==inf else dp[amt]

# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         m,n=amt+1,len(coins)
#         dp=[inf]*(amt+1)
#         dp[0]=0
#         coins.sort()

#         for i in range(m):
#             for j in range(n):
#                 if coins[j]<=i: 
#                     dp[i]=min(dp[i],1+dp[i-coins[j]])
#                 else: break

#         return -1 if dp[amt]==inf else dp[amt]

# class Solution:
#     def coinChange(self, coins: List[int], amt: int) -> int:
        
#         coins.sort()
#         dq,vis,dis=deque([0]),set([0]),0

#         while dq:
#             for _ in range(len(dq)):
#                 x=dq.popleft()
#                 if x==amt: return dis
#                 for c in coins:
#                     if x+c<=amt:
#                         if x+c in vis: continue
#                         vis.add(x+c)
#                         dq.append(x+c)
#                     else: break
#             dis+=1
#         return -1

class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        
        if amt==0: return 0
        coins.sort()
        dq,vis,dis=deque([0]),set([0]),0

        while dq:
            for _ in range(len(dq)):
                x=dq.popleft()
                for c in coins:
                    if x+c<=amt:
                        if x+c==amt: return dis+1
                        if x+c in vis: continue
                        vis.add(x+c)
                        dq.append(x+c)
                    else: break
            dis+=1
        return -1
