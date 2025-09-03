# class Solution:
#     def findCoins(self, ways: List[int]) -> List[int]:
        
#         n=len(ways)
#         ways=[1]+ways
#         dp=[1]+[0]*n
#         den=[]

#         for i in range(1,n+1):
#             if ways[i]==dp[i]+1: 
#                 den.append(i)
#                 for j in range(i,n+1):
#                     dp[j]+=dp[j-i]
#             elif ways[i]!=dp[i]: return []

#         return den

class Solution:
    def findCoins(self, ways: List[int]) -> List[int]:
        
        n=len(ways)
        ways=[1]+ways
        den=[]

        for i in range(1,n+1):
            if ways[i]==1: 
                den.append(i)
                for j in range(n,i-1,-1):
                    ways[j]-=ways[j-i]
            elif ways[i]!=0: return []

        return den
