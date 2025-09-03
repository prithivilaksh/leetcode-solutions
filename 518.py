#wrong
# dp[i]!=dp[i-j1]+dp[i-j2]+.... the could have some interesection for eg. 3 2 1 is same as 1 2 3
# we need to look at combination, not permutation, below solution works for permutation
#for eg coins=1 2 5, amt=5
# combination
# 5
# 2 2 1
# 2 1 1 1
# 1 1 1 1 1

# permutation
# 5
# 2 2 1
# 1 2 2
# 2 1 2
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 1 1 1 1 1

#wrong
# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:
#         @cache
#         def dp(amt):
#             if amt==0: return 1
#             res=0
#             for c in coins:
#                 if amt>=c:
#                     res+=dp(amt-c)
#             return res
#         return dp(amt)

# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:

#         n=len(coins)
#         @cache
#         def dp(amt,pos):
#             if amt==0: return 1
#             if pos==n: return 0
#             res=dp(amt,pos+1)
#             if amt>=coins[pos]:
#                 res+=dp(amt-coins[pos],pos)
#             return res
#         return dp(amt,0)

# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:

#         n=len(coins)
#         @cache
#         def dp(i,j):
#             if i==0: return 1
#             if j==n: return 0
#             res=dp(i,j+1)
#             if i>=coins[j]:
#                 res+=dp(i-coins[j],j)
#             return res
#         return dp(amt,0)

# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:
        
#         n=len(coins)
#         dp=[[0]*(n+1) for _ in range(amt+1)]
#         dp[0][n]=1
#         for i in range(amt+1):
#             for j in range(n-1,-1,-1):
#                 dp[i][j]=dp[i][j+1]
#                 if i>=coins[j]: dp[i][j]+=dp[i-coins[j]][j]
        
#         return dp[amt][0]

# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:
        
#         n=len(coins)
#         dp=[[0]*(n+1) for _ in range(amt+1)]
#         dp[0][n]=1
#         for j in range(n-1,-1,-1):
#             for i in range(amt+1):
#                 dp[i][j]=dp[i][j+1]
#                 if i>=coins[j]: dp[i][j]+=dp[i-coins[j]][j]
        
#         return dp[amt][0]

class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        
        n=len(coins)
        dp=[0]*(amt+1)
        dp[0]=1
        # for j in range(n-1,-1,-1):
        for j in range(n):
            for i in range(amt+1):
                if i>=coins[j]: dp[i]+=dp[i-coins[j]]
        
        return dp[amt]

#permutation - so wrong
# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:
        
#         n=len(coins)
#         dp=[0]*(amt+1)
#         dp[0]=1
#         for i in range(amt+1):
#             for j in range(n-1,-1,-1):
#                 if i>=coins[j]: dp[i]+=dp[i-coins[j]]
        
#         return dp[amt]