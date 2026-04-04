# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
        
#         n=len(piles)
#         psum=[0]*(n+1)

#         for i in range(n):
#             psum[i+1]=psum[i]+piles[i]
        
#         @cache
#         def dp(m,l):
#             if l==n: return 0
#             res=0
#             r=min(n,l+2*m)
#             for i in range(l,r):
#                 csum=psum[i+1]-psum[l]
#                 rsum=psum[-1]-psum[i+1]
#                 next=dp(max(m,i-l+1),i+1)
#                 res=max(res,csum+rsum-next)
#             return res
        
#         return dp(1,0)


# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
        
#         n=len(piles)
#         piles=[0]+piles
#         for i in range(n): piles[i+1]+=piles[i]

#         @cache
#         def dp(m,l):
#             if l==n: return 0
#             res=0
#             r=min(n,l+2*m)
#             for i in range(l,r):
#                 csum=piles[i+1]-piles[l]
#                 rsum=piles[-1]-piles[i+1]
#                 next=dp(max(m,i-l+1),i+1)
#                 res=max(res,csum+rsum-next)
#             return res
        
#         return dp(1,0)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n=len(piles)
        piles=[0]+piles
        for i in range(n): piles[i+1]+=piles[i]

        @cache
        def dp(m,l):
            if l==n: return 0
            res=0
            r=min(n,l+2*m)
            for i in range(l,r):
                next=dp(max(m,i-l+1),i+1)
                res=max(res,piles[-1]-piles[l]-next)
            return res
        
        return dp(1,0)
