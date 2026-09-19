# class Solution:
#     def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        
#         @cache
#         def dp(i):
#             if i==n: return 0

#             rt=mxh=0
#             res=inf
#             for k in range(i,n):
#                 if rt+books[k][0]>shelfWidth: break
#                 rt+=books[k][0]
#                 mxh=max(mxh,books[k][1])
#                 res=min(res,mxh+dp(k+1))
#             return res

#         n=len(books)

#         return dp(0)

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:

        n=len(books)
        dp=[inf]*(n+1)
        dp[n]=0
        for i in range(n-1,-1,-1):
            rt=mxh=0
            for k in range(i,n):
                rt+=books[k][0]
                if rt>shelfWidth:break
                mxh=max(mxh,books[k][1])
                dp[i]=min(dp[i],mxh+dp[k+1])

        return dp[0]