# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         n=len(prices)
#         @cache
#         def dp(pos,rem,ishold):
#             if pos==n: return 0
#             if ishold:
#                 return max(prices[pos]+dp(pos+1,rem,False),dp(pos+1,rem,True))
#             elif rem:
#                 return max(-prices[pos]+dp(pos+1,rem-1,True),dp(pos+1,rem,False))
#             return 0
        
#         return dp(0,2,False)


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         n=len(prices)
#         @cache
#         def dp(pos,step):
#             if pos==n or step==4: return 0
#             if step%2==0: #buy
#                 return max(-prices[pos]+dp(pos+1,step+1),dp(pos+1,step))
#             else: #sell
#                 return max(prices[pos]+dp(pos+1,step+1),dp(pos+1,step))
        
#         return dp(0,0)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         n=len(prices)
#         @cache
#         def dp(pos,step):
#             if pos==n or step==4: return 0
#             p=prices[pos] * (-1 if step%2==0 else 1)
#             return max(p+dp(pos+1,step+1),dp(pos+1,step))
        
#         return dp(0,0)



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         n=len(prices)
#         dp=[[0]*(4+1) for i in range(n+1)]

#         for i in range(n-1,-1,-1):
#             for j in range(3,-1,-1):
#                 p=prices[i] * (-1 if j%2==0 else 1)
#                 dp[i][j]=max(p+dp[i+1][j+1],dp[i+1][j])

#         return dp[0][0]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[0]*(4+1)

        for i in range(n-1,-1,-1):
            for j in range(3,-1,-1):
                p=prices[i] * (-1 if j%2==0 else 1)
                dp[j]=max(p+dp[j+1],dp[j])

        return dp[0]


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         n=len(prices)
#         hold1=sold1=hold2=sold2=-inf
#         for i in range(n):
#             sold2=max(sold2,hold2+prices[i])
#             hold2=max(hold2,sold1-prices[i])
#             sold1=max(sold1,hold1+prices[i])
#             hold1=max(hold1,-prices[i])
            
#         return max(sold1,sold2,0)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         n=len(prices)
#         sold1=sold2=0
#         hold1=hold2=-inf
#         for i in range(n):
#             sold2=max(sold2,hold2+prices[i])
#             hold2=max(hold2,sold1-prices[i])
#             sold1=max(sold1,hold1+prices[i])
#             hold1=max(hold1,-prices[i])
            
#         return sold2
            



