# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:
        
#         n=len(coins)
#         @cache
#         def helper(pos,amt):
#             if amt==0: return 1
#             if pos==n: return 0
#             count,ways=0,0
#             while pos<n:
#                 iamt=coins[pos]*count
#                 if iamt>amt: break
#                 ways+=helper(pos+1,amt-iamt)
#                 count+=1
#             return ways
        
#         return helper(0,amt)

# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:
        
#         n=len(coins)
#         @cache
#         def helper(pos,amt):
#             if amt==0: return 1
#             ways=0
#             if amt>=coins[pos]:ways+=helper(pos,amt-coins[pos])
#             if pos+1!=n: ways+=helper(pos+1,amt)
#             return ways
        
#         return helper(0,amt)

# class Solution:
#     def change(self, amt: int, coins: List[int]) -> int:
        
#         n=len(coins)
#         dp=[[0]*(n+1) for i in range(amt+1)]
        
#         for j in range(1,n+1):
#             dp[0][j]=1
#             for i in range(1,amt+1):
#                 dp[i][j]+=dp[i][j-1]
#                 if i>=coins[j-1]:
#                     dp[i][j]+=dp[i-coins[j-1]][j]

#         return dp[amt][n]


class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        
        dp=[0]*(amt+1)
        dp[0]=1
        for j in coins:
            for i in range(j,amt+1):
                dp[i]+=dp[i-j]

        return dp[amt]

