# class Solution:
#     @cache
#     def climbStairs(self, n: int) -> int:
#         if n==0: return 1
#         if n<0: return 0
#         return self.climbStairs(n-1)+self.climbStairs(n-2)

# class Solution:
#     @cache
#     def climbStairs(self, n: int) -> int:
#         if n==0 or n==1: return 1
#         return self.climbStairs(n-1)+self.climbStairs(n-2)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp=[0]*(n+1)
#         dp[0]=dp[1]=1
#         for i in range(2,n+1): dp[i]=dp[i-1]+dp[i-2]
#         return dp[n]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         p2=p1=1
#         for i in range(2,n+1): 
#             tmp=p1+p2
#             p2=p1
#             p1=tmp
#         return p1

class Solution:
    def climbStairs(self, n: int) -> int:
        p2=p1=1
        for i in range(2,n+1): 
            p2,p1=p1,p1+p2
        return p1